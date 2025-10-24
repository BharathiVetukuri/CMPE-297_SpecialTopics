import argparse
import os
from datetime import datetime
from textwrap import dedent, fill
from pathlib import Path

try:
    from fpdf import FPDF  # fpdf2
    HAVE_FPDF = True
except Exception:
    HAVE_FPDF = False

TEMPLATE = """\
# {project_title}

**Client:** {client_name}  
**Project Location:** {location}  
**Date:** {date_str}  
**Prepared By:** {contractor_name}

---

## 1. Executive Summary
{summary}

## 2. Scope of Work
{scope}

## 3. Materials & Finishes
{materials}

## 4. Project Timeline
{timeline}

## 5. Permits & Inspections
{permits}

## 6. Exclusions & Constraints
{exclusions}

## 7. Payment Schedule
{payments}

## 8. Change Orders
{change_orders}

## 9. Warranty & Post-Completion Support
{warranty}

## 10. Assumptions
{assumptions}

## 11. Deliverables
{deliverables}

---

### Acceptance & Authorization

**Client Signature:** ___________________________  **Date:** _____________

**Contractor Signature:** ________________________  **Date:** _____________

*Note:* This document is formatted for conversion to PDF and inclusion in a renovation contract.
"""

def infer_defaults_from_prompt(prompt: str):
    p = (prompt or "").lower()
    title = "Kitchen Remodel Proposal" if "kitchen" in p else "Renovation Proposal"
    location = "TBD"
    client = "Client Name"
    contractor = "Your Company, Inc."
    return title, location, client, contractor

def default_sections(title: str):
    summary = dedent(f"""\
        This proposal outlines the scope, timeline, materials, payment schedule, and warranty terms for the {title.lower()}.
        It is intended to be included as an exhibit in the final renovation contract. All dimensions and quantities are
        to be field-verified prior to procurement. Pricing and allowances can be listed in an addendum if required.
    """).strip()

    scope = dedent("""\
        • Demolition of existing finishes, cabinets, and non-load-bearing elements as marked.
        • Rough plumbing and electrical modifications to meet new layout.
        • Installation of new cabinetry, countertops, backsplash, and fixtures.
        • Flooring removal and replacement (laminate/LVP/engineered hardwood, as specified).
        • Painting of walls, ceiling, and trims; surface prep included.
        • Final fit-off for appliances, hardware, and lighting.
        • Site protection, daily cleanup, and debris disposal.
    """).strip()

    materials = dedent("""\
        • Cabinets: Shaker-style, plywood boxes, soft-close hardware.  
        • Countertops: Quartz, 3 cm, eased edge.  
        • Backsplash: Porcelain or ceramic tile, customer to select.  
        • Flooring: LVP (20-mil wear layer) or as specified.  
        • Fixtures: Pull-down faucet, undermount sink, LED cans & pendants.  
        • Paint: Low-VOC, eggshell walls / semi-gloss trim.
        *Final selections to be approved in a Finish Schedule.*
    """).strip()

    timeline = dedent("""\
        • Pre-construction (permits, ordering): 1–2 weeks  
        • On-site work (demo → finish): 4–6 weeks, subject to scope and lead times  
        • Substantial completion walk-through & punch list: ~1 week after installation
        *Schedule may shift due to inspections, change orders, or supplier delays.*
    """).strip()

    permits = dedent("""\
        Contractor will prepare required permit applications and coordinate inspections.
        Permit fees are billed at cost. Work will comply with local building codes and
        manufacturer installation requirements.
    """).strip()

    exclusions = dedent("""\
        • Discovery of concealed conditions (e.g., structural, mold, asbestos, knob-and-tube).  
        • Utility upgrades beyond stated scope.  
        • Third-party design fees, HOA approvals, or special engineering unless noted.  
        • Owner-purchased items outside the documented Finish Schedule.
    """).strip()

    payments = dedent("""\
        • 10% Deposit upon contract signing  
        • 40% Due at start of on-site work  
        • 40% Due at cabinetry & countertop install completion  
        • 10% Retainage due at final sign-off (punch list complete)
        *Invoices net-7; late payments may delay schedule.*
    """).strip()

    change_orders = dedent("""\
        Changes to scope or selections after contract execution require a written Change Order.
        Each Change Order will specify cost and schedule impact and must be approved prior to work.
    """).strip()

    warranty = dedent("""\
        One-year workmanship warranty from substantial completion. Manufacturer warranties apply
        per product terms. Damage due to misuse, neglect, or non-contractor modifications is excluded.
    """).strip()

    assumptions = dedent("""\
        • Normal working hours (Mon–Fri, 8am–5pm).  
        • Unobstructed access to work areas, water, power, and staging.  
        • Owner decisions on selections within 5 business days of request.  
        • Minor paint touch-ups expected after final install/settlement.
    """).strip()

    deliverables = dedent("""\
        • Signed contract + this Proposal Exhibit  
        • Approved drawings/measurements (if applicable)  
        • Finish Schedule (SKUs, colors, specs)  
        • Permit documents & inspection sign-offs  
        • Final invoice & warranty packet
    """).strip()

    return dict(
        summary=summary, scope=scope, materials=materials, timeline=timeline,
        permits=permits, exclusions=exclusions, payments=payments,
        change_orders=change_orders, warranty=warranty, assumptions=assumptions,
        deliverables=deliverables
    )

def render_markdown(prompt: str, project_title: str, client_name: str, location: str, contractor_name: str):
    sections = default_sections(project_title)
    md = TEMPLATE.format(
        project_title=project_title,
        client_name=client_name,
        location=location,
        date_str=datetime.now().strftime("%Y-%m-%d"),
        contractor_name=contractor_name,
        **sections
    )
    return md

def write_md(md_text: str, out_md: Path):
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(md_text, encoding="utf-8")

def write_pdf(md_text: str, out_pdf: Path):
    if not HAVE_FPDF:
        raise RuntimeError("fpdf2 not installed. Run: pip install fpdf2")

    # Very simple Markdown→PDF: strip headings to plain text, keep basic sections.
    lines = []
    for raw in md_text.splitlines():
        line = raw
        if line.startswith("#"):
            line = line.lstrip("#").strip().upper()
        lines.append(line)
    text = "\n".join(lines)

    pdf = FPDF(format="Letter", unit="pt")
    pdf.set_auto_page_break(auto=True, margin=36)
    pdf.add_page()
    pdf.add_font("DejaVu","", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", uni=True)

    pdf.add_font("DejaVu","B","/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", uni=True)

    pdf.set_font("DejaVu", size=12)
    pdf.set_font("DejaVu", size=12)

    for paragraph in text.split("\n\n"):
        wrapped = fill(paragraph, width=95)
        pdf.multi_cell(0, 16, wrapped)
        pdf.ln(4)

    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out_pdf))

def main():
    parser = argparse.ArgumentParser(description="Offline demo: generate renovation proposal (MD + PDF) without calling an LLM.")
    parser.add_argument("prompt", help="User prompt, e.g. 'Hello. Generate Proposal Document for the kitchen remodel requirement...'")
    parser.add_argument("--client", default="Client Name")
    parser.add_argument("--contractor", default="Your Company, Inc.")
    parser.add_argument("--location", default="TBD")
    parser.add_argument("--title", default=None, help="Override project title")
    parser.add_argument("--out-dir", default="outputs/proposals")
    parser.add_argument("--stem", default=None, help="Base filename stem (default uses timestamp)")
    args = parser.parse_args()

    title, loc_default, client_default, contractor_default = infer_defaults_from_prompt(args.prompt)
    project_title = args.title or title
    location = args.location if args.location != "TBD" else loc_default
    client = args.client if args.client != "Client Name" else client_default
    contractor = args.contractor if args.contractor != "Your Company, Inc." else contractor_default

    md = render_markdown(args.prompt, project_title, client, location, contractor)

    stamp = args.stem or datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = Path(args.out_dir)
    out_md = out_dir / f"{stamp}-{project_title.replace(' ', '_').lower()}.md"
    out_pdf = out_dir / f"{stamp}-{project_title.replace(' ', '_').lower()}.pdf"

    write_md(md, out_md)
    write_pdf(md, out_pdf)

    print("✅ Offline demo complete.")
    print(f"Markdown: {out_md}")
    print(f"PDF     : {out_pdf}")

if __name__ == "__main__":
    main()
