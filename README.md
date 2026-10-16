# Brookfield Clinic: AI voice agent demo

A working chat and voice assistant for a fictional private outpatient clinic,
built by [Online Marketing Help](https://onlinemarketinghelp.co.uk) so a
prospect can hear what their own callers would hear before they buy anything.

**Live: https://ohm-demo-healthcare.vercel.app**

Press the button in the corner, or "Talk to Ruth now" in the hero. It answers by
voice or by typing, at any hour.

**Putting it on the OHM site:** see [INTEGRATION.md](INTEGRATION.md). Short
version: link to it from the clinics page, do not put its widget on a page
that already has the OMH assistant.

---

## It is a demonstration, and it says so

Brookfield Clinic does not exist. The clinic, the consultants, the fees and the
phone number are invented, and the number is in Ofcom's reserved range for drama
so it cannot ring anybody. There is a banner at the top of the page saying so,
and if you ask the assistant whether it is a real company, it tells you plainly
that it is not.

In healthcare that matters more than anywhere. A convincing fake clinic with a
working phone assistant is a problem if it does not say what it is, and one that
gives clinical advice is a bigger problem. This one is built so it cannot.

---

## What is worth testing

The point of a demo is not to watch it succeed. Three things are worth trying:

**Ask what it costs.** It quotes the fee schedule and nothing else. An initial
consultation is £195, physiotherapy is £85, an ultrasound is £250. Ask whether
your policy covers something and it will tell you the insurers the clinic is
recognised by, then say that whether a specific policy covers a specific
treatment is for the insurer to confirm, not for it to guess at.

**Ask it something clinical.** "My blood test results are back, are they
alright?" or "I have a rash, should I be worried?" It will not answer. Not a
hedge, not a "probably nothing", not a reassurance. It takes the detail and gets
a clinician to ring back, and it says that is what it is doing. Reassurance is
advice, and it is not qualified to give either.

**Ask something it has not been told.** It says so and takes your details rather
than inventing an answer. That is the behaviour a cautious practice manager is
actually worried about, and it is the behaviour almost no voice agent demo
shows.

It also triages before it does anything else. Describe chest pain or
breathlessness and it tells you to ring 999 and ends the call, without stopping
to take your name first.

---

## How it is put together

```
kb/business.py        the fictional clinic: fees, clinics, insurers, triage rules
kb/build.py           turns that into knowledge base rows, pushes to Convex
retell/create-agent.py  builds the voice agent's prompt and tools
n8n/build-workflows.py  generates the four workflows
web/src/embed.js      the widget, vanilla DOM in a shadow root
web/build-site.py     the demo site itself
scripts/verify.mjs    proves it works and proves it is isolated
```

Nothing is hand written twice. The prompt, the knowledge base and the page all
read `kb/business.py`, so the agent cannot describe one clinic while the page
describes another. The triage rules sit in the prompt as well as the knowledge
base, because by the time an agent has decided to search for something, a caller
with chest pain has already waited too long.

### Four n8n workflows, this demo's own

| Workflow | What it does |
|---|---|
| Chat | the chat webhook and the agent behind it |
| Voice | Retell's tool calls, and the web call token |
| Retell Events | writes the transcript back when a call ends |
| Notify | emails the team about anything waiting |

### Backend

Convex holds the knowledge base, the fee schedule, conversations and bookings.
One deployment serves the live Online Marketing Help assistant and both industry
demos, separated by a `tenant` field. That separation is load bearing, not
cosmetic: without it a clinic would be able to answer with an estate agency's
fees. `scripts/verify.mjs` tests it on every run.

The chat agent runs on OpenRouter (Claude Haiku 5.5, falling back to GPT-4o
mini). Voice is Retell with a British voice, the same one the live assistant
uses.

---

## Running it

You need `.env.local` with the Convex, n8n, Retell and OpenRouter credentials.
It is not in this repository and must not be.

```bash
python3 kb/build.py --push              # seed the knowledge base
python3 retell/create-agent.py --push   # create or update the voice agent
python3 n8n/build-workflows.py          # generate the workflows
python3 n8n/push.py --activate          # push them and turn them on
python3 web/build-site.py && node web/build.mjs
node scripts/verify.mjs                 # 17 checks
```

`verify.mjs` is the one that matters. It asks the live assistant real questions,
checks it refuses every clinical one, and checks it cannot reach the other
tenants' content. It also clears up after itself, so running it does not email
the team about a test booking.

---

Online Marketing Help, The Hut, Central Ave, Hullbridge, Hockley SS5 6AU.
020 3489 3934.
