// app/page.tsx
import React from "react";

export default function Page() {
  return (
    <div className="min-h-screen bg-neutral-950 text-neutral-100">
      <Navbar />
      <main>
        <HeroSection />
        <TrustBar />
        <CompareROI />
        <PropertyCategories />
        <FeaturedListings />
        <ClientSecurity />
        <TransactionJourney />
        <ExitPolicy />
        <LocationGuide />
        <BuilderShowcase />
        <BuilderPricing />
        <ActiveOffers />
        <ContactForm />
      </main>
      <Footer />
      <WhatsAppButton />
    </div>
  );
}

/* ----------------------------- Shared UI bits ----------------------------- */

function Container({
  children,
  className = "",
}: {
  children: React.ReactNode;
  className?: string;
}) {
  return (
    <div className={`mx-auto w-full max-w-6xl px-5 md:px-8 ${className}`}>
      {children}
    </div>
  );
}

function Pill({ children }: { children: React.ReactNode }) {
  return (
    <span className="inline-flex items-center rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs tracking-wide text-white/80 backdrop-blur">
      {children}
    </span>
  );
}

function SectionHeader({
  kicker,
  title,
  desc,
  align = "left",
}: {
  kicker?: string;
  title: string;
  desc?: string;
  align?: "left" | "center";
}) {
  const a = align === "center" ? "text-center items-center" : "text-left";
  return (
    <div className={`flex flex-col gap-3 ${a}`}>
      {kicker ? <Pill>{kicker}</Pill> : null}
      <h2 className="text-2xl md:text-4xl font-semibold tracking-tight">
        {title}
      </h2>
      {desc ? (
        <p className="text-sm md:text-base text-white/70 max-w-2xl">
          {desc}
        </p>
      ) : null}
    </div>
  );
}

function Card({
  children,
  className = "",
}: {
  children: React.ReactNode;
  className?: string;
}) {
  return (
    <div
      className={[
        "rounded-2xl border border-white/10 bg-white/[0.04] shadow-[0_0_0_1px_rgba(255,255,255,0.03)] backdrop-blur",
        className,
      ].join(" ")}
    >
      {children}
    </div>
  );
}

function GoldLine() {
  return (
    <div className="h-px w-full bg-gradient-to-r from-transparent via-amber-200/35 to-transparent" />
  );
}

/* -------------------------------- Navbar -------------------------------- */

function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b border-white/10 bg-neutral-950/70 backdrop-blur">
      <Container className="py-4">
        <div className="flex items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <div className="h-9 w-9 rounded-xl bg-gradient-to-br from-amber-200/40 to-white/5 border border-white/10" />
            <div className="leading-tight">
              <div className="text-sm font-semibold tracking-wide">
                Dubai Property Hub
              </div>
              <div className="text-xs text-white/60">
                Luxury • ROI • Verified Deals
              </div>
            </div>
          </div>

          <nav className="hidden md:flex items-center gap-7 text-sm text-white/75">
            <a className="hover:text-white" href="#roi">
              ROI
            </a>
            <a className="hover:text-white" href="#categories">
              Categories
            </a>
            <a className="hover:text-white" href="#listings">
              Listings
            </a>
            <a className="hover:text-white" href="#locations">
              Locations
            </a>
            <a className="hover:text-white" href="#builders">
              Builders
            </a>
            <a className="hover:text-white" href="#contact">
              Contact
            </a>
          </nav>

          <div className="flex items-center gap-3">
            <a
              href="#contact"
              className="hidden sm:inline-flex items-center justify-center rounded-xl border border-white/10 bg-white/5 px-4 py-2 text-sm text-white hover:bg-white/10"
            >
              Get Brochure
            </a>
            <a
              href="#contact"
              className="inline-flex items-center justify-center rounded-xl bg-amber-200/90 px-4 py-2 text-sm font-semibold text-neutral-950 hover:bg-amber-200"
            >
              Book a Call
            </a>
          </div>
        </div>
      </Container>
    </header>
  );
}

/* --------------------------------- Hero --------------------------------- */

function HeroSection() {
  return (
    <section className="relative overflow-hidden">
      {/* Ambient gradients */}
      <div className="pointer-events-none absolute inset-0">
        <div className="absolute -top-32 left-1/2 h-[520px] w-[820px] -translate-x-1/2 rounded-full bg-amber-200/10 blur-3xl" />
        <div className="absolute top-32 -left-24 h-[420px] w-[420px] rounded-full bg-white/5 blur-3xl" />
        <div className="absolute -bottom-24 right-0 h-[520px] w-[520px] rounded-full bg-amber-200/5 blur-3xl" />
      </div>

      <Container className="relative py-16 md:py-24">
        <div className="grid items-center gap-10 md:grid-cols-2">
          <div className="flex flex-col gap-6">
            <Pill>Dubai • Premium Listings • Verified ROI</Pill>

            <h1 className="text-4xl md:text-6xl font-semibold tracking-tight">
              Luxury Real Estate,
              <span className="block text-white/80">
                curated for investors & end-users.
              </span>
            </h1>

            <p className="text-base md:text-lg text-white/70 max-w-xl">
              Explore signature towers, waterfront residences, and high-yield
              communities — with clear ROI comparisons and a secure transaction
              journey.
            </p>

            <div className="flex flex-col sm:flex-row gap-3">
              <a
                href="#listings"
                className="inline-flex items-center justify-center rounded-xl bg-amber-200/90 px-5 py-3 text-sm font-semibold text-neutral-950 hover:bg-amber-200"
              >
                View Featured Listings
              </a>
              <a
                href="#roi"
                className="inline-flex items-center justify-center rounded-xl border border-white/10 bg-white/5 px-5 py-3 text-sm text-white hover:bg-white/10"
              >
                Compare ROI
              </a>
            </div>

            <div className="grid grid-cols-3 gap-3 pt-4">
              <MiniStat label="Avg ROI Range" value="6–11%" />
              <MiniStat label="Prime Areas" value="12+" />
              <MiniStat label="Client Support" value="End-to-End" />
            </div>
          </div>

          <Card className="p-5 md:p-6">
            <div className="flex items-center justify-between">
              <Pill>Featured Insight</Pill>
              <span className="text-xs text-white/60">Updated weekly</span>
            </div>
            <div className="mt-5 space-y-4">
              <div className="rounded-2xl border border-white/10 bg-gradient-to-br from-white/5 to-transparent p-4">
                <div className="text-sm font-semibold">
                  Investor Quick Match
                </div>
                <p className="mt-1 text-sm text-white/70">
                  Tell us budget + goal, we shortlist 3 best options with ROI
                  and payment plans.
                </p>
                <div className="mt-4 grid grid-cols-2 gap-3">
                  <Input placeholder="Budget (AED)" />
                  <Input placeholder="Purpose (Rent / End-use)" />
                  <Input placeholder="Area (Marina / Downtown)" />
                  <Input placeholder="WhatsApp Number" />
                </div>
                <a
                  href="#contact"
                  className="mt-4 inline-flex w-full items-center justify-center rounded-xl bg-white text-neutral-950 px-4 py-3 text-sm font-semibold hover:bg-white/90"
                >
                  Get Shortlist on WhatsApp
                </a>
                <p className="mt-2 text-xs text-white/55">
                  No spam. We reply with 3 options + brochure links.
                </p>
              </div>

              <GoldLine />

              <div className="grid grid-cols-3 gap-3">
                <Badge title="Verified Listings" />
                <Badge title="Transparent Fees" />
                <Badge title="Secure Process" />
              </div>
            </div>
          </Card>
        </div>
      </Container>
    </section>
  );
}

function MiniStat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/[0.03] p-3">
      <div className="text-xs text-white/60">{label}</div>
      <div className="mt-1 text-sm font-semibold">{value}</div>
    </div>
  );
}

function Badge({ title }: { title: string }) {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-3 py-2 text-center text-xs text-white/75">
      {title}
    </div>
  );
}

function Input({ placeholder }: { placeholder: string }) {
  return (
    <input
      placeholder={placeholder}
      className="w-full rounded-xl border border-white/10 bg-neutral-950/40 px-3 py-2 text-sm text-white placeholder:text-white/40 outline-none focus:border-amber-200/50"
    />
  );
}

/* ------------------------------- Trust Bar ------------------------------- */

function TrustBar() {
  return (
    <section className="border-y border-white/10 bg-white/[0.02]">
      <Container className="py-6">
        <div className="grid gap-3 md:grid-cols-4">
          <TrustItem title="Dubai-ready" desc="Luxury-first design & tone" />
          <TrustItem title="Fast decisions" desc="ROI clarity & shortlists" />
          <TrustItem title="Secure journey" desc="Step-by-step process" />
          <TrustItem title="Always reachable" desc="WhatsApp-first support" />
        </div>
      </Container>
    </section>
  );
}

function TrustItem({ title, desc }: { title: string; desc: string }) {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/[0.03] px-4 py-3">
      <div className="text-sm font-semibold">{title}</div>
      <div className="text-xs text-white/60 mt-1">{desc}</div>
    </div>
  );
}

/* -------------------------------- CompareROI ----------------------------- */

function CompareROI() {
  const rows = [
    { area: "Downtown", type: "Luxury Towers", roi: "6–8%", risk: "Low" },
    { area: "Dubai Marina", type: "Waterfront", roi: "7–9%", risk: "Low" },
    { area: "Business Bay", type: "Investor Core", roi: "8–11%", risk: "Med" },
    { area: "JVC", type: "Value Growth", roi: "8–10%", risk: "Med" },
  ];

  return (
    <section id="roi" className="py-16 md:py-24">
      <Container>
        <div className="flex flex-col gap-8">
          <SectionHeader
            kicker="ROI Comparison"
            title="See the returns before you decide."
            desc="We present expected yield ranges by area and category so you can compare options like an investor."
          />

          <Card className="overflow-hidden">
            <div className="grid grid-cols-4 gap-0 border-b border-white/10 bg-white/[0.03] px-5 py-4 text-xs text-white/60">
              <div>Area</div>
              <div>Category</div>
              <div>ROI (est.)</div>
              <div>Risk</div>
            </div>
            <div className="divide-y divide-white/10">
              {rows.map((r) => (
                <div
                  key={r.area}
                  className="grid grid-cols-4 px-5 py-4 text-sm hover:bg-white/[0.03]"
                >
                  <div className="font-semibold">{r.area}</div>
                  <div className="text-white/75">{r.type}</div>
                  <div className="text-white/90">{r.roi}</div>
                  <div className="text-white/70">{r.risk}</div>
                </div>
              ))}
            </div>
          </Card>

          <div className="grid gap-4 md:grid-cols-3">
            <Card className="p-5">
              <div className="text-sm font-semibold">Rental Yield</div>
              <p className="mt-2 text-sm text-white/70">
                Compare net yield expectations with occupancy assumptions.
              </p>
            </Card>
            <Card className="p-5">
              <div className="text-sm font-semibold">Payment Plans</div>
              <p className="mt-2 text-sm text-white/70">
                Identify investor-friendly plans to preserve cashflow.
              </p>
            </Card>
            <Card className="p-5">
              <div className="text-sm font-semibold">Resale Strategy</div>
              <p className="mt-2 text-sm text-white/70">
                Align exit timing with upcoming infrastructure & demand.
              </p>
            </Card>
          </div>
        </div>
      </Container>
    </section>
  );
}

/* ---------------------------- PropertyCategories -------------------------- */

function PropertyCategories() {
  const cats = [
    { title: "Waterfront Luxury", desc: "Marina • Harbour • Canal views" },
    { title: "Downtown Signature", desc: "Iconic skyline • prime lifestyle" },
    { title: "Investor Core", desc: "Business Bay • high rental demand" },
    { title: "Family Communities", desc: "Parks • schools • value growth" },
    { title: "Off-Plan Launches", desc: "Early pricing • flexible plans" },
    { title: "Ready to Move", desc: "Immediate handover • rental-ready" },
  ];

  return (
    <section id="categories" className="py-16 md:py-24 bg-white/[0.02]">
      <Container>
        <div className="flex flex-col gap-8">
          <SectionHeader
            kicker="Categories"
            title="Choose the lifestyle. Or choose the yield."
            desc="Luxury buyers and investors need different shortlists — we separate them clearly."
          />

          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {cats.map((c) => (
              <Card key={c.title} className="p-5 hover:bg-white/[0.06]">
                <div className="flex items-start justify-between gap-4">
                  <div>
                    <div className="text-base font-semibold">{c.title}</div>
                    <div className="mt-2 text-sm text-white/70">{c.desc}</div>
                  </div>
                  <div className="h-10 w-10 rounded-xl border border-white/10 bg-gradient-to-br from-amber-200/25 to-white/5" />
                </div>
              </Card>
            ))}
          </div>
        </div>
      </Container>
    </section>
  );
}

/* ---------------------------- FeaturedListings ---------------------------- */

function FeaturedListings() {
  const listings = [
    { name: "Canal View Residence", area: "Business Bay", price: "From AED 1.2M", plan: "60/40" },
    { name: "Marina Signature Tower", area: "Dubai Marina", price: "From AED 1.8M", plan: "50/50" },
    { name: "Downtown Luxury Suites", area: "Downtown", price: "From AED 2.4M", plan: "70/30" },
    { name: "Family Green Community", area: "JVC", price: "From AED 950K", plan: "40/60" },
  ];

  return (
    <section id="listings" className="py-16 md:py-24">
      <Container>
        <div className="flex flex-col gap-8">
          <div className="flex flex-col md:flex-row md:items-end md:justify-between gap-6">
            <SectionHeader
              kicker="Featured Listings"
              title="Handpicked opportunities, not endless scrolling."
              desc="A curated selection with clear pricing, payment plan highlights, and quick WhatsApp requests."
            />
            <a
              href="#contact"
              className="inline-flex items-center justify-center rounded-xl border border-white/10 bg-white/5 px-5 py-3 text-sm text-white hover:bg-white/10"
            >
              Request Full Inventory
            </a>
          </div>

          <div className="grid gap-4 md:grid-cols-2">
            {listings.map((l) => (
              <Card key={l.name} className="p-5">
                <div className="flex gap-5">
                  <div className="h-20 w-20 shrink-0 rounded-2xl border border-white/10 bg-gradient-to-br from-white/5 to-amber-200/10" />
                  <div className="flex-1">
                    <div className="flex items-start justify-between gap-4">
                      <div>
                        <div className="text-base font-semibold">{l.name}</div>
                        <div className="mt-1 text-sm text-white/60">{l.area}</div>
                      </div>
                      <Pill>{l.plan}</Pill>
                    </div>
                    <div className="mt-3 flex items-center justify-between">
                      <div className="text-sm text-white/75">{l.price}</div>
                      <a
                        href="#contact"
                        className="text-sm font-semibold text-amber-200 hover:text-amber-100"
                      >
                        Get Brochure →
                      </a>
                    </div>
                  </div>
                </div>
              </Card>
            ))}
          </div>
        </div>
      </Container>
    </section>
  );
}

/* ----------------------------- ClientSecurity ----------------------------- */

function ClientSecurity() {
  const points = [
    { t: "Verified Documents", d: "We validate key details before you commit." },
    { t: "Transparent Process", d: "Clear steps, timelines, and responsibilities." },
    { t: "Trusted Partners", d: "Mortgage, legal, and property management support." },
  ];

  return (
    <section className="py-16 md:py-24 bg-white/[0.02]">
      <Container>
        <div className="grid gap-10 md:grid-cols-2 md:items-center">
          <div className="flex flex-col gap-6">
            <SectionHeader
              kicker="Client Security"
              title="Luxury feel. Bank-grade clarity."
              desc="Premium service means you always know what happens next — and what your money is doing."
            />
            <div className="grid gap-3">
              {points.map((p) => (
                <Card key={p.t} className="p-5">
                  <div className="text-sm font-semibold">{p.t}</div>
                  <div className="mt-2 text-sm text-white/70">{p.d}</div>
                </Card>
              ))}
            </div>
          </div>

          <Card className="p-6">
            <div className="text-sm font-semibold">Secure Checklist</div>
            <p className="mt-2 text-sm text-white/70">
              A luxury buyer experience with investor discipline.
            </p>
            <div className="mt-5 grid gap-3">
              <ChecklistItem text="Developer background & track record" />
              <ChecklistItem text="Payment plan and handover timeline" />
              <ChecklistItem text="Service charges and net yield estimate" />
              <ChecklistItem text="Resale, mortgage, and exit options" />
            </div>
            <a
              href="#contact"
              className="mt-6 inline-flex w-full items-center justify-center rounded-xl bg-amber-200/90 px-4 py-3 text-sm font-semibold text-neutral-950 hover:bg-amber-200"
            >
              Get the Checklist PDF
            </a>
          </Card>
        </div>
      </Container>
    </section>
  );
}

function ChecklistItem({ text }: { text: string }) {
  return (
    <div className="flex items-start gap-3 rounded-xl border border-white/10 bg-white/[0.03] px-4 py-3">
      <div className="mt-1 h-2.5 w-2.5 rounded-full bg-amber-200/80" />
      <div className="text-sm text-white/75">{text}</div>
    </div>
  );
}

/* -------------------------- TransactionJourney --------------------------- */

function TransactionJourney() {
  const steps = [
    { n: "01", t: "Discovery", d: "Budget, purpose, timeline, preferred areas." },
    { n: "02", t: "Shortlist", d: "3 best options with ROI + payment plan fit." },
    { n: "03", t: "Viewing / Virtual", d: "On-site tours or high-end walkthroughs." },
    { n: "04", t: "Booking", d: "Reservation, paperwork, and secure deposits." },
    { n: "05", t: "Handover", d: "Snagging, keys, and move-in or rent setup." },
    { n: "06", t: "Aftercare", d: "Property management, resale, and upgrades." },
  ];

  return (
    <section className="py-16 md:py-24">
      <Container>
        <div className="flex flex-col gap-8">
          <SectionHeader
            kicker="Transaction Journey"
            title="From first message to keys — smoothly."
            desc="A premium journey with defined steps so you stay confident at every stage."
          />

          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {steps.map((s) => (
              <Card key={s.n} className="p-5">
                <div className="flex items-center justify-between">
                  <div className="text-xs text-white/60">{s.n}</div>
                  <div className="h-9 w-9 rounded-xl border border-white/10 bg-white/5" />
                </div>
                <div className="mt-3 text-base font-semibold">{s.t}</div>
                <div className="mt-2 text-sm text-white/70">{s.d}</div>
              </Card>
            ))}
          </div>
        </div>
      </Container>
    </section>
  );
}

/* -------------------------------- ExitPolicy ------------------------------ */

function ExitPolicy() {
  return (
    <section className="py-16 md:py-24 bg-white/[0.02]">
      <Container>
        <div className="grid gap-8 md:grid-cols-2 md:items-center">
          <SectionHeader
            kicker="Exit Strategy"
            title="Plan your exit before you enter."
            desc="We help you decide whether you should rent, flip, or hold — based on your profile."
          />
          <Card className="p-6">
            <div className="text-sm font-semibold">Three Exit Options</div>
            <div className="mt-4 grid gap-3">
              <ExitItem title="Rent & Hold" desc="Stable cashflow with managed tenancy." />
              <ExitItem title="Flip on Milestones" desc="Resell near handover or demand peaks." />
              <ExitItem title="Upgrade & Resell" desc="Furnish + stage for higher market value." />
            </div>
          </Card>
        </div>
      </Container>
    </section>
  );
}

function ExitItem({ title, desc }: { title: string; desc: string }) {
  return (
    <div className="rounded-xl border border-white/10 bg-white/[0.03] px-4 py-3">
      <div className="text-sm font-semibold">{title}</div>
      <div className="mt-1 text-sm text-white/70">{desc}</div>
    </div>
  );
}

/* ------------------------------ LocationGuide ----------------------------- */

function LocationGuide() {
  const areas = [
    { a: "Downtown", b: "Iconic lifestyle & prime resale" },
    { a: "Dubai Marina", b: "Waterfront rentals & demand" },
    { a: "Business Bay", b: "Investor hub near downtown" },
    { a: "JVC", b: "Value growth + family appeal" },
  ];

  return (
    <section id="locations" className="py-16 md:py-24">
      <Container>
        <div className="flex flex-col gap-8">
          <SectionHeader
            kicker="Location Guide"
            title="Pick the right area — not just the popular one."
            desc="We match your purpose to area DNA: rental demand, lifestyle, growth, and liquidity."
          />

          <div className="grid gap-4 md:grid-cols-2">
            {areas.map((x) => (
              <Card key={x.a} className="p-5">
                <div className="flex items-start justify-between gap-4">
                  <div>
                    <div className="text-base font-semibold">{x.a}</div>
                    <div className="mt-2 text-sm text-white/70">{x.b}</div>
                  </div>
                  <div className="h-12 w-12 rounded-2xl border border-white/10 bg-gradient-to-br from-amber-200/20 to-white/5" />
                </div>
              </Card>
            ))}
          </div>
        </div>
      </Container>
    </section>
  );
}

/* ------------------------------ BuilderShowcase --------------------------- */

function BuilderShowcase() {
  const builders = [
    "Emaar (style benchmark)",
    "Damac (luxury variety)",
    "Nakheel (community scale)",
    "Sobha (premium finish)",
    "Select Group (Marina strength)",
    "Ellington (design-led)",
  ];

  return (
    <section id="builders" className="py-16 md:py-24 bg-white/[0.02]">
      <Container>
        <div className="flex flex-col gap-8">
          <SectionHeader
            kicker="Builders"
            title="Only reputable developers in your shortlist."
            desc="We prioritize reputation, delivery history, and resale strength — not just marketing."
          />

          <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {builders.map((b) => (
              <Card key={b} className="p-5">
                <div className="flex items-center gap-3">
                  <div className="h-10 w-10 rounded-xl border border-white/10 bg-white/5" />
                  <div className="text-sm font-semibold">{b}</div>
                </div>
              </Card>
            ))}
          </div>
        </div>
      </Container>
    </section>
  );
}

/* ------------------------------ BuilderPricing ---------------------------- */

function BuilderPricing() {
  return (
    <section className="py-16 md:py-24">
      <Container>
        <div className="flex flex-col gap-8">
          <SectionHeader
            kicker="Pricing"
            title="Clear tiers, luxury feel."
            desc="Pick a tier and we match it to the most suitable areas, projects, and payment plans."
          />

          <div className="grid gap-4 md:grid-cols-3">
            <PricingCard
              title="Entry Investor"
              price="AED 800K+"
              points={[
                "High-demand areas",
                "Cashflow-first shortlist",
                "Flexible payment plans",
              ]}
              highlight={false}
            />
            <PricingCard
              title="Luxury Core"
              price="AED 1.5M+"
              points={[
                "Prime skyline options",
                "Balanced ROI + lifestyle",
                "Developer preference list",
              ]}
              highlight
            />
            <PricingCard
              title="Ultra Premium"
              price="AED 3M+"
              points={[
                "Signature residences",
                "Private viewings",
                "Concierge transaction support",
              ]}
              highlight={false}
            />
          </div>
        </div>
      </Container>
    </section>
  );
}

function PricingCard({
  title,
  price,
  points,
  highlight,
}: {
  title: string;
  price: string;
  points: string[];
  highlight?: boolean;
}) {
  return (
    <Card
      className={[
        "p-6",
        highlight ? "border-amber-200/30 bg-amber-200/[0.08]" : "",
      ].join(" ")}
    >
      <div className="flex items-center justify-between">
        <div className="text-base font-semibold">{title}</div>
        {highlight ? <Pill>Most Popular</Pill> : null}
      </div>
      <div className="mt-3 text-3xl font-semibold tracking-tight">{price}</div>
      <div className="mt-5 grid gap-2">
        {points.map((p) => (
          <div key={p} className="text-sm text-white/75">
            • {p}
          </div>
        ))}
      </div>
      <a
        href="#contact"
        className={[
          "mt-6 inline-flex w-full items-center justify-center rounded-xl px-4 py-3 text-sm font-semibold",
          highlight
            ? "bg-amber-200/90 text-neutral-950 hover:bg-amber-200"
            : "border border-white/10 bg-white/5 text-white hover:bg-white/10",
        ].join(" ")}
      >
        Get Matches
      </a>
    </Card>
  );
}

/* ------------------------------- ActiveOffers ----------------------------- */

function ActiveOffers() {
  const offers = [
    { t: "Launch Offer", d: "Early-bird pricing + preferred unit selection." },
    { t: "Payment Plan", d: "Flexible installments designed for investors." },
    { t: "Premium Incentives", d: "Select projects include service charge waivers." },
  ];

  return (
    <section className="py-16 md:py-24 bg-white/[0.02]">
      <Container>
        <div className="flex flex-col gap-8">
          <SectionHeader
            kicker="Active Offers"
            title="Limited-time advantages worth knowing."
            desc="We’ll share current incentives and launch opportunities tailored to your budget."
          />

          <div className="grid gap-4 md:grid-cols-3">
            {offers.map((o) => (
              <Card key={o.t} className="p-5">
                <div className="text-base font-semibold">{o.t}</div>
                <div className="mt-2 text-sm text-white/70">{o.d}</div>
                <a
                  href="#contact"
                  className="mt-4 inline-flex text-sm font-semibold text-amber-200 hover:text-amber-100"
                >
                  Request Details →
                </a>
              </Card>
            ))}
          </div>
        </div>
      </Container>
    </section>
  );
}

/* ------------------------------- ContactForm ------------------------------ */

function ContactForm() {
  return (
    <section id="contact" className="py-16 md:py-24">
      <Container>
        <div className="grid gap-8 md:grid-cols-2 md:items-start">
          <SectionHeader
            kicker="Contact"
            title="Get a curated shortlist in 15 minutes."
            desc="Send your budget and goal. We respond with 3 best options + brochures on WhatsApp."
          />

          <Card className="p-6">
            <form
              className="grid gap-3"
              onSubmit={(e) => {
                e.preventDefault();
                alert("Submitted! Next: connect to WhatsApp / email.");
              }}
            >
              <div className="grid gap-3 sm:grid-cols-2">
                <Input placeholder="Full Name" />
                <Input placeholder="WhatsApp Number" />
              </div>
              <Input placeholder="Email (optional)" />
              <select className="w-full rounded-xl border border-white/10 bg-neutral-950/40 px-3 py-2 text-sm text-white/80 outline-none focus:border-amber-200/50">
                <option>Goal: Investment</option>
                <option>Goal: End-use</option>
                <option>Goal: Both</option>
              </select>
              <textarea
                placeholder="Tell us budget, preferred area, and timeline…"
                className="min-h-[120px] w-full rounded-xl border border-white/10 bg-neutral-950/40 px-3 py-2 text-sm text-white placeholder:text-white/40 outline-none focus:border-amber-200/50"
              />
              <button className="mt-2 inline-flex items-center justify-center rounded-xl bg-amber-200/90 px-4 py-3 text-sm font-semibold text-neutral-950 hover:bg-amber-200">
                Send Message
              </button>
              <p className="text-xs text-white/55">
                You’ll get a reply on WhatsApp. No spam, no endless follow-ups.
              </p>
            </form>
          </Card>
        </div>
      </Container>
    </section>
  );
}

/* --------------------------------- Footer -------------------------------- */

function Footer() {
  return (
    <footer className="border-t border-white/10 bg-neutral-950">
      <Container className="py-10">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
          <div>
            <div className="text-sm font-semibold">Dubai Property Hub</div>
            <div className="mt-1 text-xs text-white/60">
              Luxury listings • Verified ROI • Secure transaction journey
            </div>
          </div>
          <div className="text-xs text-white/55">
            © {new Date().getFullYear()} All rights reserved.
          </div>
        </div>
      </Container>
    </footer>
  );
}

/* ------------------------------ WhatsAppButton ---------------------------- */

function WhatsAppButton() {
  // Replace with your WhatsApp number in international format: e.g. 9715XXXXXXX
  const phone = "971500000000";
  const text = encodeURIComponent("Hi! I want a Dubai property shortlist.");
  return (
    <a
      href={`https://wa.me/${phone}?text=${text}`}
      target="_blank"
      rel="noreferrer"
      className="fixed bottom-6 right-6 z-50 inline-flex items-center gap-2 rounded-full bg-green-500 px-4 py-3 text-sm font-semibold text-white shadow-lg hover:bg-green-400"
      aria-label="Chat on WhatsApp"
    >
      WhatsApp
      <span className="h-1.5 w-1.5 rounded-full bg-white/80" />
    </a>
  );app/
 ├── page.tsx (Home)
 ├── listings/page.tsx
 ├── locations/page.tsx
 ├── about/page.tsx
 ├── contact/page.tsx
 ├── layout.tsx
components/
 ├── Navbar.tsx
 ├── PropertyCard.tsx
 ├── FilterBar.tsx
 ├── ROICalculator.tsx
 ├── WhatsAppButton.tsx
lib/
 ├── properties.ts
}export const properties = [
  {
    id: 1,
    title: "Downtown Luxury Tower",
    area: "Downtown",
    price: 2400000,
    roi: 7.5,
    type: "Luxury",
    image: "https://images.unsplash.com/photo-1600585154340-be6161a56a0c"
  },
  {
    id: 2,
    title: "Marina Waterfront Apartment",
    area: "Marina",
    price: 1800000,
    roi: 8.2,
    type: "Waterfront",
    image: "https://images.unsplash.com/photo-1502673530728-f79b4cab31b1"
  },
  {
    id: 3,
    title: "Business Bay Investor Unit",
    area: "Business Bay",
    price: 1300000,
    roi: 9.8,
    type: "Investor",
    image: "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d"
  },
  {
    id: 4,
    title: "Palm Premium Residence",
    area: "Palm",
    price: 4200000,
    roi: 6.5,
    type: "Ultra Luxury",
    image: "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6"
  }export default function PropertyCard({ property }) {
  return (
    <div className="bg-neutral-900 rounded-2xl overflow-hidden shadow-lg border border-white/10">
      <img
        src={property.image}
        alt={property.title}
        className="h-56 w-full object-cover"
      />
      <div className="p-5">
        <h3 className="text-lg font-semibold">{property.title}</h3>
        <p className="text-sm text-white/60">{property.area}</p>

        <div className="flex justify-between mt-4 text-sm">
          <span>AED {property.price.toLocaleString()}</span>
          <span>ROI {property.roi}%</span>
        </div>

        <a
          href={`https://wa.me/919880292989?text=Hi, I'm interested in ${property.title}`}
          target="_blank"
          className="block mt-4 text-center bg-amber-300 text-black py-2 rounded-xl font-semibold"
        >
          Get Details
        </a>
      </div>
    </div>
  );
}export default function FilterBar({ setFilter }) {
  return (
    <div className="flex gap-4 mb-8 flex-wrap">
      {["All", "Downtown", "Marina", "Business Bay", "Palm"].map(area => (
        <button
          key={area}
          onClick={() => setFilter(area)}
          className="px-4 py-2 bg-white/10 rounded-xl hover:bg-amber-300 hover:text-black"
        >
          {area}
        </button>
      ))}
    </div>
  );
}"use client";
import { useState } from "react";
import { properties } from "@/lib/properties";
import PropertyCard from "@/components/PropertyCard";
import FilterBar from "@/components/FilterBar";

export default function ListingsPage() {
  const [filter, setFilter] = useState("All");

  const filtered =
    filter === "All"
      ? properties
      : properties.filter(p => p.area === filter);

  return (
    <div className="min-h-screen bg-neutral-950 text-white p-10">
      <h1 className="text-3xl font-semibold mb-6">Luxury Listings</h1>

      <FilterBar setFilter={setFilter} />

      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filtered.map(property => (
          <PropertyCard key={property.id} property={property} />
        ))}
      </div>
    </div>
  );
}"use client";
import { useState } from "react";

export default function ROICalculator() {
  const [price, setPrice] = useState(0);
  const [rent, setRent] = useState(0);

  const roi = price ? ((rent * 12) / price) * 100 : 0;

  return (
    <div className="bg-neutral-900 p-6 rounded-2xl border border-white/10">
      <h3 className="text-lg font-semibold mb-4">ROI Calculator</h3>

      <input
        type="number"
        placeholder="Property Price (AED)"
        onChange={(e) => setPrice(Number(e.target.value))}
        className="w-full mb-3 p-2 rounded bg-neutral-800"
      />

      <input
        type="number"
        placeholder="Monthly Rent (AED)"
        onChange={(e) => setRent(Number(e.target.value))}
        className="w-full mb-3 p-2 rounded bg-neutral-800"
      />

      <p className="mt-4 text-amber-300 font-semibold">
        Estimated ROI: {roi.toFixed(2)}%
      </p>
    </div>
  );
}"use client";

export default function ContactPage() {

  const handleSubmit = (e) => {
    e.preventDefault();
    const name = e.target.name.value;
    const message = e.target.message.value;

    const text = encodeURIComponent(
      `Name: ${name}\nMessage: ${message}`
    );

    window.open(`https://wa.me/919880292989?text=${text}`);
  };

  return (
    <div className="min-h-screen bg-neutral-950 text-white p-10">
      <h1 className="text-3xl mb-6">Contact Us</h1>

      <form onSubmit={handleSubmit} className="max-w-md space-y-4">
        <input
          name="name"
          placeholder="Your Name"
          className="w-full p-2 rounded bg-neutral-800"
        />

        <textarea
          name="message"
          placeholder="Your Requirement"
          className="w-full p-2 rounded bg-neutral-800"
        />

        <button className="bg-amber-300 text-black px-6 py-2 rounded-xl font-semibold">
          Send via WhatsApp
        </button>
      </form>
    </div>
  );
}
];