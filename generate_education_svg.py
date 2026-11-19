import base64

def b64(filepath):
    with open(filepath, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

iitb = b64('iitbombay.png')
uis  = b64('uis.png')
mu   = b64('mu.png')

svg = f"""<svg width="900" height="270" viewBox="0 0 900 270" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="c1"><rect x="32"  y="68" width="90" height="90" rx="9"/></clipPath>
    <clipPath id="c2"><rect x="327" y="68" width="90" height="90" rx="9"/></clipPath>
    <clipPath id="c3"><rect x="622" y="68" width="90" height="90" rx="9"/></clipPath>
  </defs>

  <!-- Background -->
  <rect width="900" height="270" fill="#0b1a0f"/>

  <!-- HEADER -->
  <text x="20" y="38" font-size="22" fill="#6ab46a">&#127891;</text>
  <line x1="52" y1="18" x2="52" y2="43" stroke="#3a5a3a" stroke-width="1.5"/>
  <text x="62" y="38" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif" font-size="20" font-weight="700" fill="#dedad0">Education</text>
  <line x1="200" y1="31" x2="845" y2="31" stroke="#2a4a2a" stroke-width="1"/>
  <text x="852" y="37" font-family="monospace" font-size="13" fill="#3a5a3a">//</text>

  <!-- CARD 1: IIT Bombay -->
  <rect x="20"  y="52" width="275" height="172" rx="12" fill="#122012" stroke="#2a4a2a" stroke-width="1"/>
  <rect x="228" y="175" width="52" height="34" rx="8" fill="#1a2e1a" opacity="0.55"/>
  <rect x="32"  y="68" width="90" height="90" rx="9" fill="#f2ede0"/>
  <image href="data:image/png;base64,{iitb}" x="32" y="68" width="90" height="90" preserveAspectRatio="xMidYMid meet" clip-path="url(#c1)"/>
  <line x1="134" y1="76" x2="134" y2="150" stroke="#2a4a2a" stroke-width="1"/>
  <text x="148" y="102" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif" font-size="15" font-weight="700" fill="#ffffff">IIT Bombay</text>
  <text x="148" y="122" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif" font-size="11.5" fill="#88aa88">PG in AI &amp; Data Science</text>
  <rect x="148" y="136" width="118" height="26" rx="13" fill="#182a18"/>
  <text x="163" y="153" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif" font-size="11" fill="#78b878">&#128197;  Dec 2025</text>

  <!-- CARD 2: University of Illinois Springfield -->
  <rect x="313" y="52" width="275" height="172" rx="12" fill="#122012" stroke="#2a4a2a" stroke-width="1"/>
  <rect x="521" y="175" width="52" height="34" rx="8" fill="#1a2e1a" opacity="0.55"/>
  <rect x="327" y="68" width="90" height="90" rx="9" fill="#f2ede0"/>
  <image href="data:image/png;base64,{uis}" x="327" y="68" width="90" height="90" preserveAspectRatio="xMidYMid meet" clip-path="url(#c2)"/>
  <line x1="429" y1="76" x2="429" y2="150" stroke="#2a4a2a" stroke-width="1"/>
  <text x="443" y="94"  font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif" font-size="14" font-weight="700" fill="#ffffff">University of</text>
  <text x="443" y="112" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif" font-size="14" font-weight="700" fill="#ffffff">Illinois Springfield</text>
  <text x="443" y="128" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif" font-size="11.5" fill="#88aa88">MS Computer Science</text>
  <rect x="443" y="142" width="118" height="26" rx="13" fill="#182a18"/>
  <text x="458" y="159" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif" font-size="11" fill="#78b878">&#128197;  Dec 2023</text>

  <!-- CARD 3: University of Mumbai -->
  <rect x="606" y="52" width="275" height="172" rx="12" fill="#122012" stroke="#2a4a2a" stroke-width="1"/>
  <rect x="814" y="175" width="52" height="34" rx="8" fill="#1a2e1a" opacity="0.55"/>
  <rect x="622" y="68" width="90" height="90" rx="9" fill="#f2ede0"/>
  <image href="data:image/png;base64,{mu}" x="622" y="68" width="90" height="90" preserveAspectRatio="xMidYMid meet" clip-path="url(#c3)"/>
  <line x1="724" y1="76" x2="724" y2="150" stroke="#2a4a2a" stroke-width="1"/>
  <text x="738" y="94"  font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif" font-size="14" font-weight="700" fill="#ffffff">University of</text>
  <text x="738" y="112" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif" font-size="14" font-weight="700" fill="#ffffff">Mumbai</text>
  <text x="738" y="128" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif" font-size="11.5" fill="#88aa88">BE Computer Science</text>
  <rect x="738" y="142" width="118" height="26" rx="13" fill="#182a18"/>
  <text x="753" y="159" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif" font-size="11" fill="#78b878">&#128197;  May 2022</text>

  <!-- TIMELINE -->
  <line x1="20" y1="248" x2="880" y2="248" stroke="#2a4a2a" stroke-width="1"/>
  <circle cx="157" cy="248" r="5" fill="#122012" stroke="#5a9060" stroke-width="1.5"/>
  <circle cx="450" cy="248" r="5" fill="#122012" stroke="#5a9060" stroke-width="1.5"/>
  <circle cx="743" cy="248" r="5" fill="#122012" stroke="#5a9060" stroke-width="1.5"/>
</svg>"""

with open('education.svg', 'w') as f:
    f.write(svg)

print("Done! education.svg has been generated with logos embedded.")
