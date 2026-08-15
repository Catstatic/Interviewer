#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');
const vm = require('vm');
const crypto = require('crypto');

const root = path.resolve(__dirname, '..');
const htmlPath = path.join(root, 'mission-viva.html');
const deepPath = path.join(root, 'content', 'deep-sheets.json');
const answerPath = path.join(root, 'content', 'answer-layers.json');
const answerAliasPath = path.join(root, 'content', 'answer-aliases.json');
const orgPath = path.join(root, 'content', 'organization-dossiers.json');
const derivationPath = path.join(root, 'content', 'derivation-extensions.json');
const trapPath = path.join(root, 'content', 'trap-radar.json');
const expandedFlashcardPath = path.join(root, 'content', 'expanded-flashcards.json');
const resourcePath = path.join(root, 'content', 'resource-extensions.json');
const visualPath = path.join(root, 'content', 'visual-extensions.json');
const backupV1Path = path.join(root, 'tests', 'fixtures', 'backup-v1.json');
const malformedBackupPath = path.join(root, 'tests', 'fixtures', 'backup-malformed-nested.json');
const html = fs.readFileSync(htmlPath, 'utf8');
const sourceTemplate = fs.readFileSync(path.join(root, 'src', 'mission-viva.template.html'), 'utf8');
const sourceStyle = fs.readFileSync(path.join(root, 'src', 'mission-viva.css'), 'utf8');
const sourceScript = fs.readFileSync(path.join(root, 'src', 'mission-viva.js'), 'utf8');
const rebuiltHtml = sourceTemplate.replace('/* MV_STYLE_BUNDLE */', sourceStyle).replace('/* MV_SCRIPT_BUNDLE */', sourceScript);
const deepRaw = fs.readFileSync(deepPath);
const deepSource = JSON.parse(deepRaw);
const deepHash = crypto.createHash('sha256').update(deepRaw).digest('hex');
const answerRaw = fs.readFileSync(answerPath);
const answerSource = JSON.parse(answerRaw);
const answerHash = crypto.createHash('sha256').update(answerRaw).digest('hex');
const answerAliasRaw = fs.readFileSync(answerAliasPath);
const answerAliasSource = JSON.parse(answerAliasRaw);
const answerAliasHash = crypto.createHash('sha256').update(answerAliasRaw).digest('hex');
const orgRaw = fs.readFileSync(orgPath);
const orgSource = JSON.parse(orgRaw);
const orgHash = crypto.createHash('sha256').update(orgRaw).digest('hex');
const derivationRaw = fs.readFileSync(derivationPath);
const derivationSource = JSON.parse(derivationRaw);
const derivationHash = crypto.createHash('sha256').update(derivationRaw).digest('hex');
const trapRaw = fs.readFileSync(trapPath);
const trapSource = JSON.parse(trapRaw);
const trapHash = crypto.createHash('sha256').update(trapRaw).digest('hex');
const expandedFlashcardRaw = fs.readFileSync(expandedFlashcardPath);
const expandedFlashcardSource = JSON.parse(expandedFlashcardRaw);
const expandedFlashcardHash = crypto.createHash('sha256').update(expandedFlashcardRaw).digest('hex');
const resourceRaw = fs.readFileSync(resourcePath);
const resourceSource = JSON.parse(resourceRaw);
const resourceHash = crypto.createHash('sha256').update(resourceRaw).digest('hex');
const visualRaw = fs.readFileSync(visualPath);
const visualSource = JSON.parse(visualRaw);
const visualHash = crypto.createHash('sha256').update(visualRaw).digest('hex');
const backupV1 = JSON.parse(fs.readFileSync(backupV1Path, 'utf8'));
const malformedBackup = JSON.parse(fs.readFileSync(malformedBackupPath, 'utf8'));
const scripts = [...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/gi)];
const inlineHandlerNames = [...new Set([...html.matchAll(/\bon(?:click|change|input|pointerdown|pointerup|pointercancel|keydown|keyup)="([A-Za-z_$][\w$]*)\s*\(/g)].map(x=>x[1]).filter(x=>!['document','window','Math','if'].includes(x)))];

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

assert(rebuiltHtml === html, 'Self-contained HTML is stale relative to src/ sources');
assert(scripts.length === 1, `Expected one inline application script; found ${scripts.length}`);
assert(!html.includes('__CF$cv'), 'Cloudflare challenge injection is still present');
assert(!html.includes('/cdn-cgi/challenge-platform'), 'Cloudflare network path is still present');
assert((scripts[0][1].match(/function\s+drill\s*\(/g) || []).length === 1, 'drill() must have exactly one declaration');
assert(!html.includes('q.slice(0,300)'), 'Question browser is still limited to the first 300 records');
assert(!html.includes('42+done*3'), 'Fabricated readiness formula is still present');
assert(!html.includes('settings.apiKey=runtimeKey'), 'API key is still assigned to persistent settings');
assert(html.includes('class="skip-link"') && html.includes('Skip to main content'), 'Skip link is missing');
assert(html.includes('role="dialog"') && html.includes('aria-modal="true"') && html.includes('aria-hidden="true"'), 'Accessible dialog semantics are missing');
assert(html.includes('@media(prefers-reduced-motion:reduce)'), 'Reduced-motion CSS is missing');
assert(html.includes('@media(forced-colors:active)'), 'Forced-colours CSS is missing');
assert(html.includes('Professional interface refinement') && html.includes('backdrop-filter:blur') && html.includes('@media(max-width:640px)'), 'Professional responsive UI refinement is missing');
assert(html.includes('@media print'), 'Print stylesheet is missing');
assert(html.includes(':focus-visible'), 'Visible keyboard focus style is missing');
const railMarkup=(html.match(/<aside class="rail">([\s\S]*?)<\/aside>/)||[])[1]||'';
const permanentButtons=[...railMarkup.matchAll(/<button\b[^>]*>/g)].map(x=>x[0]);
assert(permanentButtons.length>=20 && permanentButtons.every(x=>/aria-label=/.test(x)&&/title=/.test(x)), 'Permanent navigation buttons lack accessible names/tooltips');

const elements = new Map();
function element(id = '') {
  if (elements.has(id)) return elements.get(id);
  const value = {
    id,
    innerHTML: '',
    textContent: '',
    value: '',
    checked: false,
    disabled: false,
    dataset: {},
    style: {},
    classList: { add() {}, remove() {}, contains() { return false; } },
    querySelectorAll() { return []; },
    appendChild() {},
    addEventListener() {},
    setAttribute() {},
    removeAttribute() {},
    click() {},
    focus() {},
    offsetParent: {},
    getContext() {
      return {
        beginPath() {}, moveTo() {}, lineTo() {}, stroke() {}, clearRect() {},
        save() {}, restore() {}, fillRect() {}, fillText() {},
      };
    },
    getBoundingClientRect() { return { left:0, top:0, width:650, height:320 }; },
    setPointerCapture() {},
    toDataURL() { return 'data:image/png;base64,'; },
  };
  elements.set(id, value);
  return value;
}

const storage = new Map();
const sandbox = {
  console,
  EXPECTED_DEEP_SHEETS: deepSource.topics,
  EXPECTED_DEEP_HASH: deepHash,
  EXPECTED_ANSWER_LAYERS: answerSource.layers,
  EXPECTED_ANSWER_HASH: answerHash,
  EXPECTED_ANSWER_ALIASES: answerAliasSource.aliases,
  EXPECTED_ANSWER_ALIAS_HASH: answerAliasHash,
  EXPECTED_ORG_DOSSIERS: orgSource.dossiers,
  EXPECTED_ORG_HASH: orgHash,
  EXPECTED_DERIVATION_EXTENSIONS: derivationSource.derivations,
  EXPECTED_DERIVATION_HASH: derivationHash,
  EXPECTED_TRAPS: trapSource.traps,
  EXPECTED_TRAP_HASH: trapHash,
  EXPECTED_EXPANDED_FLASHCARDS: expandedFlashcardSource.cards,
  EXPECTED_EXPANDED_FLASHCARD_HASH: expandedFlashcardHash,
  EXPECTED_RESOURCE_EXTENSIONS: resourceSource.resources,
  EXPECTED_RESOURCE_HASH: resourceHash,
  EXPECTED_VISUAL_EXTENSIONS: visualSource.diagrams,
  EXPECTED_VISUAL_HASH: visualHash,
  EXPECTED_BACKUP_V1: backupV1,
  EXPECTED_MALFORMED_BACKUP: malformedBackup,
  EXPECTED_INLINE_HANDLERS: inlineHandlerNames,
  Date,
  Math,
  JSON,
  Blob,
  Promise,
  URL: { createObjectURL() { return 'blob:test'; }, revokeObjectURL() {} },
  localStorage: {
    getItem(key) { return storage.has(key) ? storage.get(key) : null; },
    setItem(key, value) { storage.set(key, String(value)); },
    removeItem(key) { storage.delete(key); },
  },
  document: {
    getElementById(id) { return element(id); },
    querySelectorAll() { return []; },
    querySelector() { return null; },
    createElement() { return element(`created-${elements.size}`); },
    addEventListener() {},
    activeElement: element('active-element'),
    body: { appendChild() {}, dataset: {} },
    onpaste: null,
  },
  navigator: { clipboard: { writeText() { return Promise.resolve(); } } },
  location: { reload() {} },
  alert() {},
  confirm() { return false; },
  fetch() { return Promise.reject(new Error('Network disabled in smoke test')); },
  setInterval() { return 1; },
  clearInterval() {},
  setTimeout,
  clearTimeout,
};
sandbox.window = sandbox;
sandbox.window.addEventListener = () => {};

const runtimeAssertions = `
(function phase0Assertions(){
  const ok = (condition, message) => { if (!condition) throw new Error(message); };
  ok(BUILD_MANIFEST.version==='2.5.0'&&BUILD_MANIFEST.stage==='release-candidate'&&BUILD_MANIFEST.storageSchema===MV.version,'Build manifest is stale or inconsistent');
  ok(q.length > 0 && q.length < 1500, 'Generated question padding was not compacted');
  ok(QUESTION_STATS.total === q.length, 'QUESTION_STATS total is stale');
  ok(q.every(x => x[3] && x[3].id && x[3].org && x[3].difficulty), 'Question metadata is incomplete');
  ok(new Set(q.map(x => (x[0]+'|'+x[1]).toLowerCase())).size === q.length, 'Duplicate subject/question pairs remain');
  ok(q.some(x => x[3].difficulty === 'project'), 'Project difficulty metadata was not produced');
  ok(q.some(x => x[3].difficulty === 'deep'), 'Deep difficulty metadata was not produced');
  ok(q.every(x => x[3].reviewStatus === 'prompt-reviewed' && x[3].reviewedOn === EDITORIAL_REVIEW_DATE), 'Editorial review metadata is incomplete');
  ok(QUESTION_STATS.reviewed === q.length, 'Reviewed question statistics are stale');
  ok(q.every(x => ['reviewed-specific-cue','reviewed-rubric-not-model-answer'].includes(x[3].cueReview)), 'Cue review labels are incomplete');
  ok(q.every(x => /[?.!]$/.test(x[1]) && x[1].split(/\\s+/).length >= 2), 'A question is malformed or lacks terminal punctuation');
  ok(q.every(x => x[2].split(/\\s+/).length >= 6), 'A reviewed cue is too short to be useful');
  ok(FOLLOWUP_TEMPLATES.length === 36, 'Context-dependent follow-ups were not separated from standalone questions');
  ok(!q.some(x => ['Limiting cases','Estimation','Derivation interruptions','Model criticism','Units and dimensions','Boundary conditions','Symmetry','Numerical reasoning','Unfamiliar problem'].some(g => x[0] === 'Advanced Core · '+g)), 'Orphan follow-up templates remain in the standalone bank');
  const byQuestion = new Map();
  q.forEach(x => {
    const key=x[1].toLowerCase().replace(/[^a-z0-9]+/g,' ').trim();
    if (byQuestion.has(key)) ok(x[3].variantOf === byQuestion.get(key), 'Cross-lane duplicate lacks variantOf: '+x[1]);
    else byQuestion.set(key,x[3].id);
  });
  const find = (subject, question) => q.find(x => x[0]===subject && x[1]===question);
  ok(find('Semiconductor Physics','What is the Hall effect used for?')[2].includes('requires conductivity'), 'Hall-effect cue still overclaims mobility');
  ok(find('Nuclear','What is a cross section?')[2].includes('dimensions of area'), 'Cross-section cue remains physically imprecise');
  ok(find('Thermodynamics','Why does free energy decrease spontaneously at fixed T and P?')[2].includes('closed system'), 'Gibbs criterion lacks its conditions');
  ok(find('Radiation Protection','What is the difference between irradiation and radioactive contamination?'), 'Irradiation/contamination terminology was not corrected');
  ok(TRAP_CONTENT_META.sha256===EXPECTED_TRAP_HASH,'Inlined trap-radar hash does not match source JSON');
  ok(JSON.stringify(TRAPS)===JSON.stringify(EXPECTED_TRAPS),'Inlined Trap Radar differs from source JSON');
  ok(TRAPS.length===250&&new Set(TRAPS.map(x=>x.id)).size===250,'Trap Radar must contain 250 unique IDs');
  ok(new Set(TRAPS.map(x=>x.wrong.toLowerCase())).size===250,'Trap Radar contains duplicate wrong statements');
  ok(new Set(TRAPS.map(x=>x.wrong+'|'+x.recovery)).size===250,'Trap/recovery pairs are duplicated');
  ok(TRAPS.every(x=>x.why&&x.followUp&&x.tags.length&&x.status==='reviewed-distinct-v1'),'A trap fails the reviewed schema');
  ok(FLASHCARD_CONTENT_META.sha256===EXPECTED_EXPANDED_FLASHCARD_HASH,'Inlined expanded-flashcard hash does not match source JSON');
  ok(JSON.stringify(EXPANDED_FLASHCARDS)===JSON.stringify(EXPECTED_EXPANDED_FLASHCARDS),'Inlined expanded flashcards differ from source JSON');
  ok(EXPANDED_FLASHCARDS.length===658&&FLASHCARDS.length===800,'Reviewed runtime flashcard deck must total exactly 800');
  ok(new Set(FLASHCARDS.map(x=>x[0])).size===800,'Runtime flashcard IDs are not unique');
  ok(new Set(EXPANDED_FLASHCARDS.map(x=>x.front.toLowerCase())).size===658,'Expanded flashcard fronts are duplicated');
  ok(EXPANDED_FLASHCARDS.every(x=>x.front&&x.back&&x.topic&&x.type&&x.status==='reviewed-stable-v1'&&!x.mayChange),'Expanded flashcard schema is incomplete');
  ok(FLASHCARDS.every(x => !/^Review card /i.test(x[1]) && x[2].trim().length >= 5), 'Placeholder flashcard content remains');
  ok(DEEP_CONTENT_META.sha256 === EXPECTED_DEEP_HASH, 'Inlined deep-sheet hash does not match source JSON');
  ok(JSON.stringify(DEEP_SHEETS) === JSON.stringify(EXPECTED_DEEP_SHEETS), 'Inlined deep-sheet data differs from source JSON');
  ok(Object.keys(DEEP_SHEETS).length === 12, 'Expected all twelve priority complete-v1 deep sheets');
  const deepRequired=['oneMinuteCore','prerequisites','definitions','equations','derivations','limitingCases','experiments','applications','rapidQuestions','intermediateQuestions','deepQuestions','numericals','traps','speak','diagrams','deriveIt','flashcards','resources','readiness'];
  Object.entries(DEEP_SHEETS).forEach(([name,z])=>{
    ok(z.status==='complete-v1', name+' is not complete-v1');
    ok(deepRequired.every(k=>z[k]), name+' is missing a required deep field');
    ok(z.rapidQuestions.length>=30 && z.intermediateQuestions.length>=10 && z.deepQuestions.length>=5, name+' lacks required question depth');
    ok(z.numericals.length>=5 && z.derivations.length>=3 && z.diagrams.length>=3, name+' lacks numericals, derivations, or diagrams');
    ok(z.resources.every(r=>r.internetRequired && r.checkedOn), name+' resource metadata is incomplete');
  });
  ok(ANSWER_CONTENT_META.sha256 === EXPECTED_ANSWER_HASH, 'Inlined answer-layer hash does not match source JSON');
  ok(JSON.stringify(CURATED_ANSWER_LAYERS) === JSON.stringify(EXPECTED_ANSWER_LAYERS), 'Inlined answer layers differ from source JSON');
  ok(CURATED_ANSWER_LAYERS.length === 327, 'Expected 327 reviewed full answer layers across thirteen batches');
  ok(CURATED_ANSWER_LAYERS.every(x=>x.status==='reviewed-full-v1'&&x.shortAnswer&&x.modelAnswer&&x.assumptions.length>=2&&x.traps.length>=2&&x.followUps.length===5),'Reviewed answer-layer schema is incomplete');
  ok(ANSWER_ALIAS_META.sha256===EXPECTED_ANSWER_ALIAS_HASH,'Inlined answer-alias hash does not match source JSON');
  ok(JSON.stringify(CURATED_ANSWER_ALIASES)===JSON.stringify(EXPECTED_ANSWER_ALIASES),'Inlined answer aliases differ from source JSON');
  ok(CURATED_ANSWER_ALIASES.length===128&&new Set(CURATED_ANSWER_ALIASES.map(x=>answerNorm(x.question))).size===128,'Reviewed answer aliases are incomplete or duplicated');
  ok(CURATED_ANSWER_ALIASES.every(x=>x.status==='reviewed-semantic-alias-v1'&&(x.targetType==='curated-full'?CURATED_ANSWER_INDEX:DEEP_ANSWER_INDEX).get(answerNorm(x.targetQuestion))),'An answer alias target is unresolved');
  ok(answerLayerForQuestion('What is a Hohmann transfer?').status==='reviewed-deep-alias','Reviewed deep semantic alias lookup failed');
  ok(answerLayerForQuestion('Why ISRO?').status==='reviewed-full-alias','Reviewed full-layer semantic alias lookup failed');
  const coverage=answerCoverageStats();ok(coverage.full+coverage.deep+coverage.cue===q.length,'Answer coverage totals are inconsistent');
  ok(coverage.full>=100&&coverage.deep>=10&&coverage.cue>0,'Answer coverage states are unexpectedly empty');
  ok(answerLayerForQuestion('What is the physical meaning of entropy?').status==='reviewed-full-v1','Curated full answer lookup failed');ok(answerLayerForQuestion('What information does XRD provide? [Project instrument drill 1]').status==='reviewed-full-v1','Generated instrument suffix normalization failed');
  ok(ORG_CONTENT_META.sha256 === EXPECTED_ORG_HASH, 'Inlined organization-dossier hash does not match source JSON');
  ok(JSON.stringify(VERIFIED_DOSSIERS) === JSON.stringify(EXPECTED_ORG_DOSSIERS), 'Inlined organization dossiers differ from source JSON');
  ok(VERIFIED_DOSSIERS.length === 24, 'Expected twenty-four source-backed organization/company dossiers');
  ok(VERIFIED_DOSSIERS.every(d=>d.stableFacts.length>=3&&d.technicalFit.length>=4&&d.interviewFocus.length>=4&&d.officialSources.length>=2),'Organization dossier schema is incomplete');
  const orgStats=dossierStats();ok(orgStats.dossiers===24&&orgStats.facts>=72&&orgStats.sources>=54,'Organization dossier statistics are invalid');
  ok(dossierCategory('bel')==='defence'&&dossierCategory('igcar')==='nuclear'&&dossierCategory('csir-nal')==='space'&&dossierCategory('tifr')==='research'&&dossierCategory('pixxel')==='space'&&dossierCategory('digantara')==='space','Organization category mapping is invalid');
  ok(orgStats.current+orgStats.stale+orgStats.unverified===orgStats.sources&&orgStats.mutable>0,'Organization source-state accounting is invalid');
  ok(resolveDossier('ISRO').id==='isro'&&resolveDossier('barc-dae').name==='BARC / DAE','Dossier resolver failed');
  ok(DERIVATION_CONTENT_META.sha256===EXPECTED_DERIVATION_HASH,'Inlined derivation-extension hash does not match source JSON');
  ok(JSON.stringify(DERIVATION_EXTENSIONS)===JSON.stringify(EXPECTED_DERIVATION_EXTENSIONS),'Inlined derivation extensions differ from source JSON');
  const derivations=allDerivations();
  ok(derivations.length===50&&new Set(derivations.map(x=>x.id)).size===50,'Derivation Dojo must contain 50 unique IDs');
  ok(derivations.every(x=>x.assumptions.length&&x.steps.length>=5&&x.interpretation&&x.unitCheck&&x.commonMistake&&x.panelInterruption&&x.summary),'A derivation fails the full schema');ok(derivations.every(x=>derivationVisual(x)),'A derivation lacks a linked visual');
  ok(!('apiKey' in settings), 'Persistent settings still contain an API key');
  ['pitch','projectQuestions','projectBoard','projectReadiness','saveProjectProfile','projectHistory','projectFieldHistory','exportProjectReview','projectChallengeScorecard','openPrerequisiteGraph','hrAnswer','scenario','dossier','filterContent','saveLivePostmortem','revisions','redactDataClass','exportPreflightCalendar'].forEach(name => ok(typeof eval(name) === 'function', name+' handler is missing'));
  const missingInlineHandlers=EXPECTED_INLINE_HANDLERS.filter(name=>{try{return typeof eval(name)!=='function'}catch(e){return true}});ok(!missingInlineHandlers.length,'Inline handlers are undefined: '+missingInlineHandlers.join(', '));
  ok(PROJECT_FIELD_SCHEMA.length >= 25, 'Structured project field schema is incomplete');
  ok(projectData().supervisor.state === 'known' && projectData().supervisor.value === 'RC Nath', 'Known supervisor default is missing');
  ok(projectData().material.state === 'unknown', 'Unknown material must remain explicitly unknown');
  ok(projectData().synthesisMethod.state==='known'&&projectData().synthesisMethod.value.includes('Grinding and firing')&&projectData().plannedTechniques.state==='planned'&&projectData().nextExperiment.state==='planned','User-confirmed grinding/firing and characterization context was not preserved');
  ok(projectReadiness().unknown > 0 && !projectReadiness().ready, 'Incomplete project was incorrectly marked ready');
  const safePitch=projectPitchText(90);
  ok(safePitch.includes('will not invent it') && !/undefined|null/i.test(safePitch), 'Pitch does not preserve unknown project facts safely');ok(projectPitchText(90,'isro').includes('For ISRO')&&projectPitchText(90,'isro').includes('official sources'),'Target-lens project pitch failed');
  ok(projectQuestionRecords().every(x => x[3].projectRelevant && x[3].difficulty === 'project'), 'Personalized project-board metadata is invalid');
  ok(normalizeTargetProfiles().length===5&&activeTargets().length===5,'Default organization target profiles are incomplete');
  const isroEvidence=targetEvidence(activeTargets().find(x=>x.id==='isro'));ok(Number.isFinite(isroEvidence.score)&&isroEvidence.topics.length===5&&targetTopicMap('barc').includes('Nuclear Physics and Radiation Protection'),'Target-specific evidence mapping failed');
  const ss=subjectStrategyStats();ok(ss.counts.declared===3&&ss.counts.prepared===2&&ss.counts.survival===7&&ss.ready.length===0,'Default declared-subject strategy is invalid');
  ok(nearestTarget()===null&&normalizeTargetProfiles().every(t=>targetDays(t)===null),'Undated targets produced a false countdown');
  const weakSignals=skillSignals();ok(weakSignals.length===8&&weakSignals.every((x,i)=>!i||weakSignals[i-1].score<=x.score),'Skill signals are missing or unsorted');
  const planIds=dailyPlan().map(x=>x.id);ok(planIds.includes('project-ledger')&&planIds.includes('srs-due')&&(!(orgStats.stale+orgStats.unverified)||planIds.includes('org-check')),'Adaptive plan omitted urgent project, SRS, or source work');ok(saved.planHistory?.length===1&&saved.planHistory[0].actions.length>0,'Daily plan history/rollover failed');
  ok(mistakeDrillType('conceptual').includes('First-principles')&&mistakeDrillType('units').includes('Dimensional'),'Exam mistake conversion map is invalid');
  ok(Object.keys(PREFLIGHT_PHASES).length===5&&Object.values(PREFLIGHT_PHASES).flat().length===20,'Pre-flight phase template is incomplete');
  ok(PRIVATE_ROLE_FAMILIES.length===9&&PRIVATE_ROLE_FAMILIES.every(r=>r.topics.length===3&&r.skills.length===3),'Private-space role-family map is incomplete');
  ok(PRIVATE_ROLE_FAMILIES.every(r=>Number.isFinite(privateRoleScore(r))),'Private-role evidence score is invalid');
  ok(preflightState('isro').venue===''&&Object.keys(preflightState('isro').checks).length===0,'Pre-flight default state is invalid');
  const validBackup={format:'MISSION_VIVA_BACKUP',version:MV.version,progress:{evidence:[]},settings:{theme:'default'}};
  ok(validateBackupObject(validBackup).ok, 'Valid backup was rejected');
  ok(!validateBackupObject({...validBackup,format:'OTHER'}).ok, 'Unknown backup format was accepted');
  ok(!validateBackupObject({...validBackup,version:MV.version+1}).ok, 'Future backup version was accepted');
  ok(!validateBackupObject({...validBackup,settings:{apiKey:'forbidden'}}).ok, 'Credential-bearing backup was accepted');
  ok(validateBackupObject(EXPECTED_BACKUP_V1).ok,'Valid version-1 fixture was rejected');const migratedBackup=migrateBackupObject(EXPECTED_BACKUP_V1);ok(migratedBackup.version===2&&migratedBackup.progress.flashcards&&!migratedBackup.progress.cards&&migratedBackup.progress.backupMigrations.length===1&&migratedBackup.settings.subjectStrategyNeedsReview,'Version-1 backup migration failed');
  ok(!validateBackupObject(EXPECTED_MALFORMED_BACKUP).ok,'Nested credential fixture was accepted');
  let replaceTarget={old:true};replaceRecord(replaceTarget,{safe:1,__proto__:{polluted:true}});ok(replaceTarget.safe===1&&!replaceTarget.old&&!({}).polluted,'Safe record replacement failed');
  applyTheme('contrast');ok(document.body.dataset.theme==='contrast','High-contrast theme did not apply');applyTheme('default');
  const openReq=buildAIRequest('hello',null,{provider:'openai',endpoint:'https://example.com/v1',model:'test-model',key:'session-key'});
  ok(openReq.url==='https://example.com/v1/chat/completions'&&openReq.body.model==='test-model'&&openReq.headers.Authorization==='Bearer session-key','OpenAI-compatible request adapter is invalid');
  const ollamaReq=buildAIRequest('hello',null,{provider:'ollama',endpoint:'http://127.0.0.1:11434',model:'local'});
  ok(ollamaReq.url.endsWith('/api/chat')&&ollamaReq.provider==='ollama','Ollama request adapter is invalid');
  let blockedHttp=false,missingGeminiKey=false;try{buildAIRequest('x',null,{provider:'openai',endpoint:'http://example.com/v1'})}catch(e){blockedHttp=true}try{buildAIRequest('x',null,{provider:'gemini',endpoint:'https://example.com',key:''})}catch(e){missingGeminiKey=true}
  ok(blockedHttp&&missingGeminiKey,'AI endpoint or session-key policy failed');
  const reviewObject=validateAIReview(parseAIJSONObject('prefix {"correctIdeas":["one"],"concerns":[],"missingStructure":["boundary"],"modelAnswer":"answer","nextQuestion":"why?","verificationWarnings":[],"confidence":"medium"} suffix'));
  ok(reviewObject.confidence==='medium'&&reviewObject.nextQuestion==='why?','Structured AI review parsing failed');
  let invalidReview=false;try{validateAIReview({confidence:'certain'})}catch(e){invalidReview=true}ok(invalidReview,'Invalid AI review schema was accepted');
  const vision=validateVisionReview({visibleElements:['axis'],concerns:[],missingLabels:['unit'],geometryIssues:[],modelInterpretation:'A graph.',followUp:'What is the limit?',verificationWarnings:['Check scale.'],confidence:'low'});ok(vision.confidence==='low'&&vision.missingLabels.length===1,'Strict vision-review schema failed');
  let invalidVision=false;try{validateVisionReview({confidence:'certain'})}catch(e){invalidVision=true}ok(invalidVision,'Invalid vision review schema was accepted');
  settings.onlineEnabled=true;runtimeKey='temporary';disableOnlineCopilot();ok(!settings.onlineEnabled&&runtimeKey===''&&activeAIControllers.size===0,'AI kill switch failed');
  ok(srsStats().newCount === FLASHCARDS.length && srsStats().due === FLASHCARDS.length, 'New SRS cards must begin due');
  const t0=1_000_000_000_000;
  const good1=scheduleFlashState(null,'good',t0),good2=scheduleFlashState(good1,'good',t0);
  const again=scheduleFlashState(good2,'again',t0),hard=scheduleFlashState(null,'hard',t0),easy=scheduleFlashState(null,'easy',t0);
  ok(good1.intervalDays===1 && good2.intervalDays===3, 'Good learning steps are invalid');
  ok(again.intervalDays===0 && again.due===t0+10*SRS_MINUTE && again.lapses===1, 'Again relearning schedule is invalid');
  ok(hard.intervalDays===1 && hard.ease<2.5, 'Hard schedule is invalid');
  ok(easy.intervalDays===4 && easy.ease>2.5, 'Easy schedule is invalid');let longState=null,longNow=t0;for(let n=0;n<12;n++){longState=scheduleFlashState(longState,'good',longNow);longNow=longState.due}ok(longState.intervalDays>30&&longState.ease>=1.3&&longState.history.length===12,'Long-horizon SRS simulation failed');let leechState=null;for(let n=0;n<8;n++)leechState=scheduleFlashState(leechState,'again',t0+n*SRS_MINUTE);ok(leechState.lapses===8,'Leech lapse simulation failed');
  const srsTestId=FLASHCARDS[0][0];flash(srsTestId);revealFlashcard(srsTestId);reviewFlashcard(srsTestId,'good');
  ok(saved.flashcards[srsTestId].intervalDays===1 && saved.flashcards[srsTestId].history.length===1, 'SRS review was not stored');
  undoFlashReview();ok(!saved.flashcards[srsTestId], 'SRS undo did not restore new-card state');
  beginFlashSession('new','definition');ok(srsSession.queue.length===10&&srsSession.queue.every(id=>flashcardMeta(id).type==='definition'),'Type-filtered SRS session failed');
  ok(srsForecast(14).length===14&&srsForecast(14)[0].count>0,'SRS forecast failed');const controlCard=FLASHCARDS[20][0];toggleSuspendFlashcard(controlCard);ok(flashState(controlCard).suspended&&!dueFlashcards().some(c=>c[0]===controlCard),'Suspended card remained due');toggleSuspendFlashcard(controlCard);ok(!flashState(controlCard).suspended,'Card unsuspend failed');
  const cm=communicationMetrics('Um, I think this is basically correct because evidence supports it. However, the limit matters.',60);
  ok(cm.words>10&&cm.fillers>=2&&cm.hedges>=1&&cm.wpm===cm.words&&cm.clearEnding&&cm.paceBand.length===2,'Communication metrics are invalid');const repetitive=communicationMetrics('The model works because evidence matters. The model works because calibration matters. So yeah',30);ok(repetitive.repeatedPhrases.length>0&&repetitive.weakEnding&&!repetitive.clearEnding,'Repeated-phrase or weak-ending metric failed');
  ok(Object.keys(STRESS_LEVELS).length===11,'Progressive stress profiles are incomplete');
  stressSettings().stressIntensity='gentle';startStress('failedResult');ok(activeDrillMode.includes('Failed-result')&&seconds>=100,'Stress intensity or failed-result profile failed');stressSettings().stressIntensity='standard';
  startStress('wrongPremise');ok(activeDrillMode.includes('Wrong premise')&&activeChallenge.includes('premise'),'Wrong-premise stress mode failed');
  const trap0=TRAPS[0],trap1=TRAPS[1];openTrap(trap0.id);document.getElementById('trapCorrection').value='A formula needs symbols, assumptions, and physical meaning.';revealTrap(trap0.id);recordTrapOutcome(trap0.id,'caught');
  ok(trapProgress(trap0.id).caught===1&&trapStatus(trap0.id)==='caught','Caught-trap evidence did not persist');
  ok(revisionItems().some(x=>x.type==='trap'&&x.itemId===trap0.id),'Trap revision was not scheduled');ok(trapCategoryPerformance().length===25&&trapCategoryPerformance().some(x=>x.attempts),'Trap category performance failed');
  practiceTrap(trap1.id);ok(trapProgress(trap1.id).timedDrills===1&&activeDrillMode==='trap recovery','Trap-to-timed-drill integration failed');activeTrapId='';

  project();pitch(90);projectQuestions();projectChallengeScorecard();['falsification','negative','alternative','ownership','reproducibility'].forEach(id=>{document.getElementById('project-challenge-score-'+id).value='3';document.getElementById('project-challenge-note-'+id).value='Unknown until confirmed; identify the next evidence.'});saveProjectChallengeScorecard();ok(saved.projectChallenges.length===1&&saved.projectChallenges[0].status==='self-recorded-not-independent','Project challenge scorecard failed');projectBoard();
  hr(); hrAnswer('intro'); scenario();
  watch();document.getElementById('signalOrg').value='Test Organization';document.getElementById('signalStatement').value='User-checked temporary programme statement.';document.getElementById('signalUrl').value='https://example.com/official';document.getElementById('signalVerified').value='2026-08-15';document.getElementById('signalExpires').value='2026-08-30';addSignalCard();ok(signalCards().length===1&&['current','stale'].includes(signalCardState(signalCards()[0])),'Manual current-fact card validation failed');dossier('ISRO');organizationFactProvenance('isro',0);openOrgFactCard('isro',0);document.getElementById('orgFactAttempt').value='A partial fact recall.';revealOrgFactCard('isro',0);recordOrgFactCard('isro',0,'missed');ok(saved.orgFactCards['isro:0'].missed===1&&revisionItems().some(x=>x.type==='organization'),'Source-aware organization card failed');organizationDrill('isro');privateTrack();evidenceLedger();
  bridge();document.getElementById('bridgeTarget').value='GATE';document.getElementById('bridgeMock').value='Mock 1';document.getElementById('bridgeWeak').value='Electromagnetism';document.getElementById('bridgeMilestone').value='Next mock';document.getElementById('bridgeConcepts').value='Boundary conditions';saveBridge();
  document.getElementById('mistakeType').value='units';document.getElementById('mistakeTopic').value='Electromagnetism';document.getElementById('mistakeNote').value='Mixed SI units';addExamMistake();
  ok(bridgeData().mistakes.length===1&&bridgeData().mistakes[0].drill.includes('Dimensional'),'Exam mistake was not converted and stored');launchMistakeDrill(bridgeData().mistakes[0].id);ok(activeDrillMode.includes('exam bridge'),'Converted exam mistake did not launch a drill');
  toggleBridgeCheck('technical',true);ok(!!bridgeData().checklist.technical,'Bridge checklist did not persist');
  togglePreflight('isro','d30|0',true);ok(!!preflightState('isro').checks['d30|0'],'Pre-flight checklist did not persist');
  board(5,'all');ok(boardQs.length===4&&boardDeadline>boardStart&&saved.inProgressBoard?.stage==='active','Mini-board timing or resume setup failed');ok(!boardQs.some((x,i)=>boardQs.slice(i+1).some(y=>semanticallyNear(x,y))),'Board contains semantic near-duplicates');
  for(let bi=0;bi<4;bi++){document.getElementById('boardAnswer').value='This answer defines the principle because evidence supports it, with an assumption and a clear limit.';boardNext()}
  ok(boardPending&&boardPending.answers.length===4&&boardPending.answers.every(x=>x.metrics.words>0),'Board answers or communication metrics were not captured');
  ['boardTechnical','boardStructure','boardComposure','boardRecovery','boardHonesty'].forEach(id=>document.getElementById(id).value='4');
  saveBoardPostmortem();ok(saved.boardHistory.length===1&&saved.boardHistory[0].scores.honesty===4&&!saved.inProgressBoard,'Board post-mortem was not saved or resume state not cleared');
  liveroom();document.getElementById('liveMode').value='ISRO';document.getElementById('liveDuration').value='custom';document.getElementById('liveCustomDuration').value='2';beginLive();ok(live.mode==='ISRO'&&live.end-live.questionAt>=119900&&live.end-live.questionAt<=120000&&saved.inProgressLive?.mode==='ISRO','Custom live-room duration or persistence failed');livePause();document.getElementById('liveAnswer').value='A concise answer with a principle, evidence, and limitation.';document.getElementById('liveQuestion').textContent='Test live question?';submitLive();ok(live.answers.length===1&&live.answers[0].seconds>=1&&live.answers[0].metrics.words>0,'Live answer timing/metrics failed');endLive();ok(saved.pendingLivePostmortem&& !saved.inProgressLive,'Unsaved live post-mortem was not persisted');['liveTech','liveStructure','liveComposure','liveRecovery','liveOrganization','liveDiagram','liveOwnership','liveHonesty'].forEach(id=>document.getElementById(id).value='4');saveLivePostmortem();ok(saved.liveHistory.length===1&&saved.liveHistory[0].pauses===1&&saved.liveHistory[0].scores.organization===4&&!saved.pendingLivePostmortem,'Live event transcript/post-mortem failed');
  contentlib();
  ok(RESOURCE_CONTENT_META.sha256===EXPECTED_RESOURCE_HASH&&JSON.stringify(RESOURCE_EXTENSIONS)===JSON.stringify(EXPECTED_RESOURCE_EXTENSIONS),'Inlined resource extensions differ from source JSON');
  ok(RESOURCE_EXTENSIONS.length===22&&RESOURCE_EXTENSIONS.every(x=>x.checkedOn&&x.level&&x.expectedUse&&x.learningMode),'Resource extension schema is incomplete');
  const resourceRows=allResources();ok(resourceRows.length===114&&new Set(resourceRows.map(x=>x.url)).size===114,'Resource Library unique-link count is invalid');ok(resourceRows.every(x=>x.title&&x.url&&x.scope&&x.topic&&x.type&&x.expectedUse),'Resource Library metadata is incomplete');resources();
  ok(VISUAL_CONTENT_META.sha256===EXPECTED_VISUAL_HASH&&JSON.stringify(VISUAL_EXTENSIONS)===JSON.stringify(EXPECTED_VISUAL_EXTENSIONS),'Inlined visual extensions differ from source JSON');
  const visualRows=allVisuals();ok(VISUAL_EXTENSIONS.length===64&&visualRows.length===100&&new Set(visualRows.map(x=>x.title.toLowerCase())).size===100,'Visual Library must contain 100 distinct original references');
  ok(visualRows.every(x=>x.svg&&x.say&&x.status==='reviewed-original-v1'&&x.checklist.length===5),'Visual Library schema is incomplete');visuals();openVisual(visualRows[0].id);revealVisualReference(visualRows[0].id);recordVisualComparison(visualRows[0].id);ok(visualProgress(visualRows[0].id).compared===1,'Visual comparison evidence was not saved');closeModal();
  const formulas=allFormulae();ok(formulas.length===153&&new Set(formulas.map(x=>x.id)).size===153,'Formula Vault record count or IDs are invalid');formulaVault();openFormula(formulas[0].id);document.getElementById('formulaAttempt').value='Formula, symbols, units, and assumptions recalled.';revealFormula(formulas[0].id);recordFormulaOutcome(formulas[0].id,'known');ok(formulaProgress(formulas[0].id).known===1,'Formula recall evidence did not persist');ok(formulaLinks(formulas[0]).derivation&&formulaLinks(formulas[0]).limit&&formulaLinks(formulas[0]).numerical&&formulaLinks(formulas[0]).experiment&&formulaLinks(formulas[0]).card,'Formula cross-links are incomplete');ok(revisionItems().some(x=>x.type==='formula'&&x.itemId===formulas[0].id),'Formula revision was not scheduled');
  dojo();const firstDerivation=allDerivations()[0];openDerivation(firstDerivation.id,0);revealDerivationStep();markDerivationError();
  while(derivationReveal<firstDerivation.steps.length)revealDerivationStep();recordDerivationAttempt('pass');
  ok(derivationProgress(firstDerivation.id).passed&&derivationProgress(firstDerivation.id).errors[0]===1,'Derivation attempt/error evidence did not persist');ok(revisionItems().some(x=>x.type==='derivation'&&x.itemId===firstDerivation.id&&x.part==='0'),'Failed derivation step revision was not scheduled');
  drawTopic('Test diagram');ok(!!drawingState('topicCanvas'),'Accessible drawing canvas did not initialize');document.getElementById('drawingLabel').value='x axis';addDrawingLabel('topicCanvas');ok(drawingState('topicCanvas').strokes[0].type==='label','Drawing label tool failed');document.getElementById('drawingAlt').value='A complete text description with axes, labels, and boundary conditions.';document.getElementById('draw-check-axes').checked=true;document.getElementById('draw-check-variables').checked=true;saveDrawingEvidence('Test diagram');ok(saved.drawingEvidence.length===1&&saved.drawingEvidence[0].hasOwnProperty('alt'),'Drawing text-alternative evidence did not persist');
  setupCanvas();ok(!!drawingState('drawCanvas'),'Live drawing canvas did not initialize with reusable controls');
  openPrerequisiteGraph();ok(document.getElementById('modalbody').innerHTML.includes('PREREQUISITE GRAPH'),'Prerequisite graph failed');Object.keys(DEEP_SHEETS).forEach(name => DEEP_TABS.forEach(tab => deepTopic(name,tab[0])));
  recordDeepPass('Solid State Physics','rapid',0);recordDeepNeedsReview('Solid State Physics','rapid',1);ok(deepProgress('Solid State Physics').failures['rapid:1']&&revisionItems().some(x=>x.type==='deep'),'Deep-sheet failure did not enter revision queue');recordDeepPass('Solid State Physics','rapid',1);ok(deepProgress('Solid State Physics').failures['rapid:1'].recoveredOn,'Deep-sheet recovery was not recorded');openDeepExternalReview('Solid State Physics','rapid',1);document.getElementById('deepReviewerRole').value='teacher';document.getElementById('deepReviewerOutcome').value='pass';document.getElementById('deepReviewerName').value='Test reviewer';document.getElementById('deepReviewerNote').value='Reviewed against stated scope.';saveDeepExternalReview('Solid State Physics','rapid',1);ok(deepProgress('Solid State Physics').reviews['rapid:1'][0].role==='teacher','External deep-sheet review evidence failed');
  startSubjectTree('Solid State Physics');for(let level=0;level<5;level++){document.getElementById('subjectTreeAnswer').value='A first-principles answer with an assumption and a test.';nextSubjectTree()}ok(saved.subjectTrees.length===1&&saved.subjectTrees[0].answers.length===5,'Declared-subject follow-up tree failed');
  qbank();
  answerCoach(0);
  document.getElementById('answerDraft').value='A saved practice answer with enough words to test local answer history.';
  saveAnswerCoachAttempt(0);
  ok(saved.answerCoachHistory.length===1&&saved.answerCoachHistory[0].status==='full','Answer Coach attempt/history status was not saved');
  startAnswerCorrection(0);document.getElementById('correctionFirst').value='An incomplete first answer.';revealAnswerCorrection();document.getElementById('correctionIssue').value='mechanism';document.getElementById('correctionNote').value='Explain path and phase.';retryAnswerCorrection();document.getElementById('correctionRetry').value='The reflected paths acquire an optical path and interface phase difference under coherent illumination.';saveAnswerCorrection();ok(saved.answerCorrections.length===1&&saved.answerCorrections[0].retryWords>5,'Wrong-answer correction sequence failed');
  openAnswerRevision(0,'specialist');document.getElementById('answerRevisionText').value='A user-authored specialist revision with equation, assumptions, units, evidence, and a limiting case.';saveAnswerRevision(0,'specialist');ok(saved.answerRevisions.length===1&&saved.answerRevisions[0].status==='user-authored-not-reviewed','Editable answer revision failed');
  questionQA();
  finalqa();

  const originalFetch=globalThis.fetch;
  globalThis.__AI_ASYNC__=(async()=>{
    globalThis.fetch=async()=>({ok:true,status:200,statusText:'OK',headers:{get:()=>null},text:async()=>JSON.stringify({choices:[{message:{content:'MISSION VIVA MOCK OK'}}]})});
    const text=await aiChat('mock',null,{force:true,provider:'openai',endpoint:'https://example.com/v1',model:'mock',key:'session'});
    ok(text==='MISSION VIVA MOCK OK','Mocked OpenAI-compatible response extraction failed');
    globalThis.fetch=async()=>({ok:false,status:429,statusText:'Too Many Requests',headers:{get:()=>null},text:async()=>'{"error":"quota"}'});
    let httpRejected=false;try{await aiChat('mock',null,{force:true,provider:'openai',endpoint:'https://example.com/v1',model:'mock',key:'session'})}catch(e){httpRejected=/HTTP 429/.test(e.message)}
    ok(httpRejected,'AI HTTP errors are not surfaced');
    globalThis.fetch=async()=>({ok:true,status:200,statusText:'OK',headers:{get:()=>null},text:async()=>'not-json'});
    let malformedRejected=false;try{await aiChat('mock',null,{force:true,provider:'openai',endpoint:'https://example.com/v1',model:'mock',key:'session'})}catch(e){malformedRejected=/malformed JSON/.test(e.message)}
    ok(malformedRejected,'Malformed provider JSON was accepted');
    globalThis.fetch=originalFetch;
  })();

  globalThis.__PHASE0_RESULT__ = {
    questions: q.length,
    difficulties: Object.fromEntries(['core','deep','project','rapid'].map(d => [d, q.filter(x => x[3].difficulty === d).length])),
    traps: TRAPS.length,
    trapCategories: new Set(TRAPS.map(x=>x.category)).size,
    flashcards: FLASHCARDS.length,
    overviews: Object.keys(FULL_SHEETS).length,
    deepSheets: Object.keys(DEEP_SHEETS).length,
    deepRapidQuestions: Object.values(DEEP_SHEETS).reduce((n,z)=>n+z.rapidQuestions.length,0),
    deepDerivations: Object.values(DEEP_SHEETS).reduce((n,z)=>n+z.derivations.length,0),
    followupTemplates: FOLLOWUP_TEMPLATES.length,
    reviewedPrompts: q.filter(x => x[3].reviewStatus === 'prompt-reviewed').length,
    curatedFullAnswers: CURATED_ANSWER_LAYERS.length,
    answerCoverage: answerCoverageStats(),
    organizationDossiers: VERIFIED_DOSSIERS.length,
    organizationSources: dossierStats().sources,
    organizationChecksDue: dossierStats().stale+dossierStats().unverified,
    derivationDojo: allDerivations().length,
    resources: allResources().length,
    visuals: allVisuals().length,
    revisionItems: revisionItems().length,
    handlers: 'ok'
  };
})();
`;

vm.createContext(sandbox);
vm.runInContext(scripts[0][1] + runtimeAssertions, sandbox, { filename: 'mission-viva-inline.js', timeout: 10_000 });
Promise.resolve(sandbox.__AI_ASYNC__).then(() => {
  console.log('Phase 0 smoke test passed:', JSON.stringify(sandbox.__PHASE0_RESULT__));
}).catch(error => {
  console.error(error);
  process.exitCode = 1;
});
