"""Genera sitio-hub/clase-44/index.html (slides animadas de la Clase 44) a partir de los textos verificados.

Fuente de verdad: este script + la Spec aprobada. No editar el HTML a mano: edita aquí y vuelve a ejecutar.
Ejecutar: py -3 -X utf8 construir_slides.py
Estructura (4 conceptos): 1 LLM (estocástico) · 2 tokens · 3 probabilidad y azar con la BOLSA DE FICHAS
· 4 evidenciarlo en la práctica (ChatGPT) + Haz Ahora, Para pensar y resumen. (Sin interactivo final: Diego lo descartó.)
"""
import json
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
DESTINO = AQUI.parents[1] / "sitio-hub" / "clase-44" / "index.html"

TEXTO_BASE = "nos vemos en el patio . nos vemos en el patio . nos vemos en la plaza . ya llegué al casino ."
CHAT = ["nos vemos en el recreo", "nos vemos en el kiosco", "llego en la micro"]


def siguientes(texto):
    p = texto.split()
    t = {}
    for a, b in zip(p, p[1:]):
        t.setdefault(a, Counter())[b] += 1
    return t


T = siguientes(TEXTO_BASE)
assert T["en"] == Counter({"el": 2, "la": 1}) and T["nos"] == Counter({"vemos": 3}) and T["el"] == Counter({"patio": 2})
assert "biblioteca" not in T and len(TEXTO_BASE.split()) == 23 and len(set(TEXTO_BASE.split())) == 12
C = siguientes(" . ".join(CHAT))
assert C["nos"] == Counter({"vemos": 2}) and C["en"] == Counter({"el": 2, "la": 1})

PLANTILLA = r'''<!doctype html>
<html lang="es-CL">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Clase 44 · Cómo funciona ChatGPT</title>
<style>
:root{--bg:#f6f7fb;--card:#fff;--ink:#0f172a;--muted:#475569;--line:#cbd5e1;--accent:#1d4ed8;--accent-ink:#fff;
--a:#b45309;--abg:#fef3c7;--p:#1d4ed8;--pbg:#dbeafe;--ok:#065f46;--okbg:#d1fae5;--bad:#b91c1c;--badbg:#fee2e2;--v:#7c3aed;--vbg:#ede9fe}
@media (prefers-color-scheme:dark){:root{--bg:#0b1220;--card:#111a2e;--ink:#e5e7eb;--muted:#94a3b8;--line:#334155;--accent:#93c5fd;--accent-ink:#0b1220;
--a:#fcd34d;--abg:#451a03;--p:#93c5fd;--pbg:#1e3a5f;--ok:#a7f3d0;--okbg:#064e3b;--bad:#fca5a5;--badbg:#450a0a;--v:#c4b5fd;--vbg:#2e1065}}
*{box-sizing:border-box}
[hidden]{display:none!important}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.55 "Segoe UI",Roboto,Arial,sans-serif}
.wrap{max-width:940px;margin:0 auto;padding:0 16px 48px}
nav.tabs{display:flex;gap:8px;padding:12px 0;flex-wrap:wrap;border-bottom:1px solid var(--line)}
nav.tabs a{padding:8px 14px;border-radius:10px;border:2px solid var(--line);color:inherit;text-decoration:none;font-weight:600}
nav.tabs a[aria-current="page"]{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
h1{font-size:1.2rem;margin:16px 0 0}
h2{font-size:1.45rem;margin:.2rem 0 .5rem}
.slide{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;margin:14px 0;min-height:460px}
.tagline{margin:0 0 .5rem;font-size:.85rem;color:var(--muted)}
.muted{color:var(--muted)}
.ctrl{display:flex;gap:10px;align-items:center;justify-content:space-between;flex-wrap:wrap}
button{font:inherit;min-height:44px;padding:8px 14px;border-radius:10px;border:2px solid var(--accent);background:var(--card);color:var(--ink);cursor:pointer}
button.primary{background:var(--accent);color:var(--accent-ink)}
button:disabled{opacity:.4;cursor:default}
button[aria-pressed="true"]{background:var(--pbg)}
:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.dots{display:flex;gap:8px;flex-wrap:wrap}
.dots button{min-height:28px;width:28px;padding:0;border-radius:99px;border:2px solid var(--accent);background:var(--card)}
.dots button[aria-current="true"]{background:var(--accent)}
.note{background:var(--abg);border-left:5px solid var(--a);padding:10px 14px;border-radius:8px;margin:12px 0}
.good{background:var(--okbg);border-left-color:var(--ok)}
.bad{background:var(--badbg);border-left-color:var(--bad)}
.info{background:var(--pbg);border-left-color:var(--p)}
code{font-family:Consolas,Menlo,monospace}
.pair{display:flex;gap:14px;flex-wrap:wrap}.pair>div{flex:1;min-width:260px}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0}
.tok{display:inline-block;padding:4px 9px;margin:3px;border:2px solid var(--p);background:var(--pbg);color:var(--p);border-radius:8px;font-weight:700;font-family:Consolas,Menlo,monospace;animation:pop .35s both}
.tok.still{animation:none;transition:all .25s}
.tok.pt{border-color:var(--line);background:var(--card);color:var(--muted)}
.tok.hl{border-color:var(--a);background:var(--abg);color:var(--a)}
.tok.nx{border-color:var(--ok);background:var(--okbg);color:var(--ok)}
.tok.big{font-size:1.3rem}
.tok.pulse{animation:pulse 1s ease-in-out 2;transform:scale(1.15)}
@keyframes pop{from{opacity:0;transform:scale(.7)}to{opacity:1;transform:none}}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 var(--a)}50%{box-shadow:0 0 0 8px transparent}}
.bubble{background:var(--bg);border:1px solid var(--line);border-radius:14px 14px 14px 2px;padding:8px 12px;margin:6px 0;max-width:420px}
.hbar{height:24px;border-radius:6px;background:var(--pbg);border:1px solid var(--line);overflow:hidden;margin:4px 0}
.hbar i{display:block;height:100%;background:var(--accent);transition:width .5s}
.hbar i.o{background:var(--a)}
.row{display:flex;align-items:center;gap:10px;margin:6px 0}.row b{min-width:90px}.row .hbar{flex:1}
.badge{display:inline-block;padding:3px 10px;border-radius:99px;font-weight:700;border:2px solid}
.badge.prob{border-color:var(--a);background:var(--abg);color:var(--a)}
.big{font-size:1.6rem;font-weight:700}
/* concepto 1 */
.llm{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0}
.lcard{flex:1;min-width:110px;text-align:center;border:2px solid var(--accent);border-radius:12px;padding:6px;background:var(--pbg);animation:pop .5s both}
.lcard b{display:block;font-size:2rem;line-height:1.1;color:var(--accent)}.lcard span{display:block;font-weight:700}.lcard em{color:var(--muted)}
.flow{display:flex;gap:8px;align-items:stretch;flex-wrap:wrap;margin:10px 0}
.zone{flex:3;min-width:240px;border:2px dashed var(--line);border-radius:12px;padding:8px}
.zt{font-weight:700;margin-bottom:4px}
.model{flex:1;min-width:110px;border:3px solid var(--accent);border-radius:16px;text-align:center;padding:10px;transition:box-shadow .4s,background .4s;font-size:1.4rem}
.model.on{background:var(--pbg);box-shadow:0 0 0 6px var(--pbg),0 0 26px var(--accent)}
.arrow{align-self:center;font-size:1.5rem;color:var(--muted)}
/* concepto 2 */
.wordbox{position:relative;display:inline-block;padding:18px 6px 6px;margin:8px 0}
.pc{display:inline-block;padding:6px 12px;border:2px solid;font:700 1.5rem Consolas,Menlo,monospace;margin:0;border-radius:0;transition:margin .6s,border-radius .6s,transform .6s}
.pc:first-child{border-radius:10px 0 0 10px}.pc:last-child{border-radius:0 10px 10px 0}.pc:only-child{border-radius:10px}
.pc+.pc{border-left-width:0}
.pc.cut{margin-right:14px;border-radius:10px;border-left-width:2px;transform:translateY(-4px)}
.c0{border-color:var(--p);background:var(--pbg);color:var(--p)}.c1{border-color:var(--a);background:var(--abg);color:var(--a)}.c2{border-color:var(--v);background:var(--vbg);color:var(--v)}
.sc{position:absolute;left:0;top:-14px;font-size:1.8rem;opacity:0}
.sc.go{animation:snip .55s linear forwards}
@keyframes snip{from{left:0;opacity:1}to{left:85%;opacity:1}}
.counter{font-size:2.2rem;font-weight:800;color:var(--accent)}
/* concepto 3: la bolsa */
.bagwrap{display:flex;gap:14px;flex-wrap:wrap;align-items:flex-start}
.bagcol{flex:1;min-width:260px}
.bagt{font-weight:700;margin:2px 0}
.bag{border:3px solid var(--a);border-radius:10px 10px 50px 50px;min-height:92px;padding:8px 14px 14px;background:var(--abg);display:flex;flex-wrap:wrap;align-content:flex-start;gap:2px}
.lane{border:2px solid var(--line);border-radius:12px;padding:6px 10px;margin:6px 0;min-height:52px}
.ficha{display:inline-block;min-width:34px}
details.v{border:2px solid var(--ok);border-radius:10px;padding:6px 12px;margin-top:12px;background:var(--okbg)}
details.v summary{cursor:pointer;font-weight:700}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
</style>
</head>
<body>
<div class="wrap">
<nav class="tabs" aria-label="Clases">
<a href="../clase-41/">Clase 41</a>
<a href="../clase-42/">Clase 42</a>
<a href="../clase-42b/">Clase 42b</a>
<a href="../clase-43-v2/">Clase 43 v2</a>
<a href="./" aria-current="page">Clase 44</a>
<a href="../">Inicio</a>
</nav>
<h1>Clase 44 · Cómo funciona ChatGPT</h1>
<p class="muted" style="margin:.2rem 0">Resumen animado: modelo de lenguaje, tokens, la bolsa de fichas y la evidencia en la práctica. Avanza con los botones o con las flechas del teclado.</p>

<section class="slide" id="slide" aria-live="polite"></section>

<div class="ctrl">
<button id="prev">← Anterior</button>
<div class="dots" id="dots" role="group" aria-label="Ir a la slide"></div>
<button id="next" class="primary">Siguiente →</button>
</div>
</div>

<script>
const TEXTO=__TEXTO__;
const CHAT=__CHAT__;
const P=TEXTO.split(' ');
const CONOC=[...new Set(P)].sort();
const T={};
for(let i=0;i<P.length-1;i++){const a=P[i],b=P[i+1];T[a]=T[a]||{};T[a][b]=(T[a][b]||0)+1}
const S=document.getElementById('slide');
let cur=0,timers=[];
const clear=()=>{timers.forEach(clearTimeout);timers=[]};
const later=(f,ms)=>timers.push(setTimeout(f,ms));
const pct=(n,t)=>Math.round(100*n/t)+' %';
const $=id=>document.getElementById(id);
function sig(w){const o=T[w];if(!o)return null;const items=Object.entries(o).sort((a,b)=>b[1]-a[1]);return{tot:items.reduce((s,x)=>s+x[1],0),items}}
/* la bolsa de una palabra: una ficha por cada vez que la siguió; si nunca la vio: una ficha por cada palabra que conoce */
function bolsa(w){const s=sig(w);if(s){const a=[];s.items.forEach(([x,n])=>{for(let i=0;i<n;i++)a.push(x)});return a}return CONOC.slice()}
function sacar(w){const b=bolsa(w);return b[Math.floor(Math.random()*b.length)]}
const chip=(w,c)=>`<span class="tok ${c||''}">${w}</span>`;
const verif=(qs)=>`<details class="v"><summary>✅ Verificamos lo aprendido</summary><ul style="margin:.4rem 0">${qs.map(q=>`<li>${q}</li>`).join('')}</ul></details>`;

const slides=[
/* 1 · Haz Ahora 1-3 */
function(){
  let modo='nos';
  const draw=()=>{
    const hl=modo==='nos'?'nos':'en';
    const bub=CHAT.map(m=>{const w=m.split(' ');return `<div class="bubble">${w.map((x,i)=>{const prev=w[i-1];const c=x===hl?'hl':(prev===hl?'nx':'pt');return chip(x,c+' still')}).join('')}</div>`}).join('');
    S.innerHTML=`<h2>El teclado quiere aprender del chat</h2>
    <p class="tagline">Haz Ahora · preguntas 1 a 3</p>
    <p>Quien programa el teclado le mostró este chat cortito del curso. Queremos saber <b>qué palabra viene después</b>.</p>
    <div class="chips"><button id="b1" aria-pressed="${modo==='nos'}">Mirar «nos»</button><button id="b2" aria-pressed="${modo==='en'}">Contar «en»</button></div>
    ${bub}
    <div class="note">${modo==='nos'?'Después de <b>«nos»</b>, siempre viene <b>«vemos»</b>: ¿qué sugerirías?':'<b>«en»</b> aparece <b>3 veces</b>. De esas, <b>2</b> veces viene «el» y <b>1</b> viene «la».'}</div>`;
    $('b1').onclick=()=>{modo='nos';draw()};
    $('b2').onclick=()=>{modo='en';draw()};
  };draw();
},
/* 2 · Haz Ahora 4 */
function(){
  const pel=['Coco','Intensamente','Moana','Encanto'];
  const hc=[],ha=[];
  const draw=()=>{
    S.innerHTML=`<h2>Calculadora y amigo</h2>
    <p class="tagline">Haz Ahora · pregunta 4</p>
    <p>Hazles la <b>misma pregunta</b> varias veces y mira qué pasa.</p>
    <div class="pair">
    <div><h3 style="margin:.2rem 0">🧮 Calculadora: «7 × 8»</h3><button id="pc" class="primary">Preguntar</button><p class="big">${hc.map(x=>'<span class="tok">'+x+'</span>').join('')}</p></div>
    <div><h3 style="margin:.2rem 0">🧑 Amigo: «recomiéndame una película»</h3><button id="pa" class="primary">Preguntar</button><p class="big">${ha.map(x=>'<span class="tok hl">'+x+'</span>').join('')}</p></div></div>
    <div class="note">¿Qué diferencia notas entre las dos? <span class="muted">(La respuesta, en los conceptos 1 y 3.)</span></div>`;
    $('pc').onclick=()=>{hc.push(56);draw()};
    $('pa').onclick=()=>{ha.push(pel[Math.floor(Math.random()*pel.length)]);draw()};
  };draw();
},
/* 3 · Concepto 1: LLM estocástico */
function(){
  const LL=[['L','Large','grande'],['L','Language','lenguaje'],['M','Model','modelo']];
  S.innerHTML=`<h2>¿Qué es un modelo de lenguaje (LLM)?</h2>
  <p class="tagline">Concepto 1 del cuaderno</p>
  <div class="llm">${LL.map((x,i)=>`<div class="lcard" style="animation-delay:${i*.3}s"><b>${x[0]}</b><span>${x[1]}</span><em>${x[2]}</em></div>`).join('')}</div>
  <ul style="margin:.4rem 0">
    <li>Aprendió, leyendo textos, a <b>predecir la siguiente palabra</b>.</li>
    <li>Es <b>estocástico</b>: su comportamiento <b>no se puede predecir con total exactitud</b>; o sea, tiene <b>azar</b> 🎲.</li>
    <li>Mira cómo aprende el de juguete 👇</li></ul>
  <div class="flow">
    <div class="zone"><div class="zt">📄 Nuestra «base de datos»</div><div id="txt"></div><div class="hbar"><i id="pg" style="width:0"></i></div><small id="cnt" class="muted">0 de ${P.length} palabras leídas</small></div>
    <div class="arrow">➜</div>
    <div class="model" id="mod">🧠<br><b>Modelo</b><br><small id="ms" class="muted">esperando…</small></div>
    <div class="arrow">➜</div>
    <div class="zone"><div class="zt">⌨️ Teclado</div><div id="out" class="muted">nos vemos en el … ?</div></div>
  </div>
  <div class="chips"><button id="go" class="primary">▶ Aprender</button><button id="rs">Reiniciar</button></div>
  <div class="note info">📱 El teclado del celular es un LLM <b>chiquito</b>; 💬 <b>ChatGPT</b> es uno <b>gigante</b>. <b>Los dos tienen azar</b>: lo que responden depende del azar y de las probabilidades con que se entrenaron.</div>
  ${verif(['¿Qué significa la sigla <b>LLM</b> y por qué decimos que es <b>estocástico</b>?','¿En qué se parece el teclado del celular a ChatGPT?'])}`;
  const txt=$('txt');
  const pintar=()=>{txt.innerHTML=P.map((w,i)=>`<span class="tok still pt" id="w${i}">${w}</span>`).join('')};
  pintar();
  const reset=()=>{clear();pintar();$('pg').style.width='0';$('cnt').textContent='0 de '+P.length+' palabras leídas';$('mod').classList.remove('on');$('ms').textContent='esperando…';$('out').innerHTML='nos vemos en el … ?'};
  $('rs').onclick=reset;
  $('go').onclick=()=>{reset();$('mod').classList.add('on');$('ms').textContent='leyendo…';
    P.forEach((w,i)=>later(()=>{const e=$('w'+i);if(e)e.className='tok still nx';$('pg').style.width=(100*(i+1)/P.length)+'%';$('cnt').textContent=(i+1)+' de '+P.length+' palabras leídas'},i*110));
    later(()=>{$('ms').textContent='¡aprendió!';$('out').innerHTML='nos vemos en el '+chip('patio','hl')+' <span class="muted">← una sugerencia (con azar)</span>'},P.length*110+300)};
},
/* 4 · Concepto 2: tokens */
function(){
  let m='mini',w=1;
  const ej=[['casa',['casa']],['inteligencia',['inteli','gencia']],['murciélago',['mur','ciél','ago']]];
  const draw=()=>{
    S.innerHTML=`<h2>Tokens: los trozos (fichas) que lee el modelo</h2>
    <p class="tagline">Concepto 2 del cuaderno</p>
    <p>El modelo no lee letras: <b>parte el texto en trozos llamados tokens</b>. Cada token es como una <b>ficha</b>.</p>
    <div class="chips"><button id="b1" aria-pressed="${m==='mini'}">Nuestro mini modelo</button><button id="b2" aria-pressed="${m==='real'}">Modelos grandes (ilustración)</button></div>
    ${m==='mini'?`<div id="tk"></div><p class="counter" id="cn">0 tokens</p><div class="note">En el mini modelo, <b>1 palabra = 1 token</b> (el <code>.</code> también).</div>`
    :`<div class="chips">${ej.map((e,i)=>`<button data-w="${i}" aria-pressed="${i===w}">${e[0]}</button>`).join('')}</div>
      <div class="wordbox"><span id="sc" class="sc">✂️</span><span id="pz">${ej[w][1].map((t,i)=>`<span class="pc c${i%3}">${t}</span>`).join('')}</span></div>
      <p class="counter" id="cn">1 pieza</p>
      <div class="chips"><button id="cut" class="primary">✂️ Cortar en tokens</button></div>
      <div class="note">En los modelos grandes, las palabras largas o poco comunes se <b>cortan en trozos</b>. Es solo una ilustración: cada modelo corta a su manera.</div>`}
    ${verif(['¿Qué es un <b>token</b>? ¿Cuántos tokens tiene nuestra base de datos en el mini modelo?','En los modelos grandes, ¿un token es siempre una palabra completa?'])}`;
    $('b1').onclick=()=>{clear();m='mini';draw()};
    $('b2').onclick=()=>{clear();m='real';draw()};
    if(m==='mini'){const box=$('tk');P.forEach((x,i)=>later(()=>{box.insertAdjacentHTML('beforeend',chip(x,x==='.'?'pt':''));$('cn').textContent=(i+1)+' tokens'},i*80))}
    else{
      document.querySelectorAll('[data-w]').forEach(b=>b.onclick=()=>{w=+b.dataset.w;draw()});
      $('cut').onclick=()=>{const sc=$('sc');sc.classList.remove('go');void sc.offsetWidth;sc.classList.add('go');
        later(()=>{document.querySelectorAll('.pc').forEach(p=>p.classList.add('cut'));const n=ej[w][1].length;$('cn').textContent=n+(n===1?' token':' tokens')},550)};
    }
  };draw();
},
/* 5 · Concepto 3: la bolsa de fichas (probabilidad + azar) */
function(){
  let w='en',k=0,probs=false,sacadas=[],ult=-1;
  const reset=()=>{clear();k=0;probs=false;sacadas=[];ult=-1};
  const draw=()=>{
    const F=bolsa(w),s=sig(w),llena=k>=F.length;
    const texto=P.map((x,i)=>{let c='pt';if(s&&k>0){if(x===w)c='hl';else if(P[i-1]===w)c='nx'}return chip(x,c+' still')}).join('');
    const tally={};sacadas.forEach(x=>tally[x]=(tally[x]||0)+1);
    S.innerHTML=`<h2>Probabilidad y azar: la bolsa de fichas</h2>
    <p class="tagline">Concepto 3 del cuaderno</p>
    <div class="note info"><b>Las respuestas de un LLM son azarosas.</b> El proceso para verlo: el modelo guarda una <b>bolsa de fichas</b> por palabra, calcula <b>probabilidades</b> y <b>saca una ficha al azar</b>.</div>
    <p>Elige una palabra y sigue los 3 pasos: <b>①</b> llenar su bolsa · <b>②</b> ver sus probabilidades · <b>③</b> sacar una ficha al azar.</p>
    <div class="chips">${['en','nos','el','biblioteca'].map(o=>`<button data-w="${o}" aria-pressed="${o===w}">${o}</button>`).join('')}</div>
    <div>${texto}</div>
    <div class="bagwrap"><div class="bagcol">
      <p class="bagt">🎒 ${s?`Bolsa de «${w}»`:`«${w}» nunca apareció: bolsa con todas las palabras que sí conoce`}</p>
      <div class="bag">${F.slice(0,k).map((x,i)=>chip(x,(i===ult?'hl pulse':'nx')+' still')).join('')||'<span class="muted">vacía</span>'}</div>
      <div class="chips"><button id="s1" class="primary">① Llenar la bolsa</button><button id="s2" ${llena?'':'disabled'}>② Ver probabilidades</button><button id="s3" ${llena?'':'disabled'}>③ 🎲 Sacar una ficha</button></div></div>
    <div class="bagcol">
      ${probs?`<p class="bagt">Probabilidad = proporción de fichas</p>${(s?s.items:CONOC.map(x=>[x,1])).map(([a,n])=>`<div class="row"><b>«${a}»</b><div class="hbar"><i class="${n===Math.max(...(s?s.items:[[0,1]]).map(x=>x[1]))?'':'o'}" style="width:${100*n/F.length}%"></i></div><span>${n} de ${F.length} = ${pct(n,F.length)}</span></div>`).join('')}`:'<p class="muted">Pulsa ② cuando la bolsa esté llena.</p>'}
      <div class="lane"><b>Fichas sacadas:</b> ${sacadas.map(x=>chip(x,'big hl still')).join('')||'<span class="muted">aún ninguna</span>'}</div>
      <p class="muted" style="margin:0">${Object.entries(tally).map(([a,n])=>'«'+a+'» '+n).join(' · ')}</p>
    </div></div>
    ${!s?`<div class="note bad"><b>«${w}»</b> nunca apareció: no tiene bolsa propia. No se queda callado: <b>saca una ficha al azar entre las palabras que sí conoce</b> (responde cualquier cosa, sin base).</div>`
    :sacadas.length?`<div class="note good">${s.items.length>1?'La más probable sale <b>más seguido</b>, pero <b>no siempre</b>: cualquier ficha de la bolsa puede salir. Eso es ser <b>estocástico</b>: lo que responde es <b>azaroso</b> y depende de las <b>probabilidades con que se entrenó</b>.':'En esta bolsa todas las fichas son iguales, pero el modelo sigue sacando una ficha al azar: el mecanismo es el mismo.'}</div>`
    :`<div class="note">📝 La ficha que <b>más veces siguió</b> es la más grande de la bolsa: es la más probable, <b>pero no la segura</b>.</div>`}
    ${verif(['En la bolsa de <code>en</code> (2 fichas <code>el</code> y 1 <code>la</code>): ¿qué probabilidad tiene cada una? ¿Por qué puede salir <code>la</code> aunque <code>el</code> sea más probable?','Si preguntamos por una palabra que el modelo nunca vio, ¿qué hace? ¿De qué depende lo que responde un modelo?'])}`;
    document.querySelectorAll('[data-w]').forEach(b=>b.onclick=()=>{reset();w=b.dataset.w;draw()});
    $('s1').onclick=()=>{reset();draw();for(let j=1;j<=F.length;j++)later(()=>{k=j;draw()},j*450)};
    $('s2').onclick=()=>{probs=true;draw()};
    $('s3').onclick=()=>{ult=Math.floor(Math.random()*F.length);sacadas.push(F[ult]);draw()};
  };draw();
},
/* 6 · Concepto 4: evidenciarlo en la práctica (la misma pregunta, dos respuestas) */
function(){
  const R1=['Te','recomiendo','ir','al','cine','el','sábado'];
  const R2=['Te','recomiendo','caminar','por','el','parque','el','sábado'];
  S.innerHTML=`<h2>Evidenciarlo en la práctica: ChatGPT también es azaroso</h2>
  <p class="tagline">Concepto 4 del cuaderno</p>
  <ol style="margin:.3rem 0"><li>El profesor envía <b>dos veces</b>, en conversaciones nuevas, el mismo prompt: <b>«Explica las diferencias entre ChatGPT, Claude y Gemini»</b>.</li>
  <li>Observamos las dos respuestas.</li><li>Anotamos qué <b>cambió</b>, qué se <b>mantuvo</b> y <b>por qué</b>.</li></ol>
  <p class="muted" style="margin:.2rem 0">Así se separan los caminos (ilustración inventada con otra pregunta):</p>
  <p><b>Pregunta:</b> «Recomiéndame un panorama para el fin de semana»</p>
  <p><b>Respuesta 1:</b> <span id="r1"></span></p>
  <p><b>Respuesta 2:</b> <span id="r2"></span></p>
  <div class="note" id="nt">Las dos <b>empiezan igual</b>…</div>
  <div class="chips"><button id="pl" class="primary">▶ Reproducir de nuevo</button></div>
  <div class="note info">En tu cuaderno: ¿qué <b>cambió</b>? ¿qué se <b>mantuvo</b>? ¿por qué? Usa <b>citas textuales</b> y la palabra <b>estocástico</b>.</div>
  ${verif(['¿Qué cambió y qué se mantuvo entre las dos respuestas? ¿Cómo lo explica que ChatGPT sea <b>estocástico</b>?','¿Por qué dos respuestas de ChatGPT a la misma pregunta pueden ser distintas?'])}`;
  const play=()=>{clear();$('r1').innerHTML='';$('r2').innerHTML='';$('nt').innerHTML='Las dos <b>empiezan igual</b>…';
    const n=Math.max(R1.length,R2.length);
    for(let i=0;i<n;i++)later(()=>{
      if(i<R1.length)$('r1').insertAdjacentHTML('beforeend',chip(R1[i],i<2?'':'hl'));
      if(i<R2.length)$('r2').insertAdjacentHTML('beforeend',chip(R2[i],i<2?'':'nx'));
      if(i===2)$('nt').innerHTML='…pero en la tercera palabra el modelo <b>sacó otra ficha</b> y ese camino se fue <b>acumulando</b>. Por eso las respuestas cambian: es <b>estocástico</b>.'},i*600)};
  $('pl').onclick=play;play();
},
/* 8 · Para pensar */
function(){
  let r=false;
  const draw=()=>{
    S.innerHTML=`<h2>🤔 Para pensar</h2>
    <p class="tagline">Para pensar</p>
    <p class="big">¿Por qué ChatGPT puede dar respuestas distintas a la misma pregunta?</p>
    <div class="chips"><button id="b" class="primary">${r?'Ocultar':'Ver la idea'}</button></div>
    ${r?`<div class="note good">Porque es <b>estocástico</b>: su comportamiento <b>no se puede predecir con total exactitud</b>, hay <b>azar</b>. En cada paso <b>saca una ficha</b> de su bolsa: la más probable sale más seguido, pero no siempre. Lo que responde depende del azar y de las probabilidades con que se entrenó. Y lo mismo pasa con nuestro modelo chiquito. La calculadora, en cambio, es <b>determinística</b>: misma entrada, siempre la misma salida.</div>`:''}`;
    $('b').onclick=()=>{r=!r;draw()};
  };draw();
},
/* 9 · resumen */
function(){
  S.innerHTML=`<h2>¿Qué aprendimos?</h2>
  <p class="tagline">Cierre</p>
  <ul>
  <li><b>LLM = Large Language Model</b> (modelo de lenguaje grande): aprende de textos a <b>predecir la siguiente palabra</b> y es <b>estocástico</b> (tiene azar). El teclado es uno chiquito; ChatGPT, uno gigante.</li>
  <li><b>Token:</b> un trozo de texto (una ficha) que el modelo lee como una sola pieza.</li>
  <li><b>Probabilidad:</b> cada palabra tiene una <b>bolsa de fichas</b>; probabilidad = proporción de fichas («2 de 3» ≈ 67 %).</li>
  <li><b>Estocástico:</b> el modelo <b>saca una ficha al azar</b>: la más probable sale más seguido, pero no siempre. Lo que responde es <b>azaroso</b> y depende de las probabilidades con que se entrenó.</li>
  <li><b>Palabra nunca vista:</b> no tiene bolsa propia, pero igual responde: saca al azar entre las palabras que sí conoce.</li>
  <li><b>Evidencia en la práctica:</b> la misma pregunta a ChatGPT, dos veces, da respuestas distintas.</li></ul>
  <div class="note good"><b>Ojo:</b> el jueves 19 es la <b>Prueba 1</b> y antes habrá un repaso. Y el lunes 23: <b>prompting</b>.</div>`;
}];

/* ---------- navegación ---------- */
const dots=$('dots');
slides.forEach((_,i)=>{const b=document.createElement('button');b.setAttribute('aria-label','Slide '+(i+1));b.onclick=()=>go(i);dots.appendChild(b)});
function go(i){clear();cur=Math.max(0,Math.min(slides.length-1,i));slides[cur]();
  [...dots.children].forEach((b,j)=>b.setAttribute('aria-current',j===cur));
  $('prev').disabled=cur===0;$('next').disabled=cur===slides.length-1}
$('prev').onclick=()=>go(cur-1);
$('next').onclick=()=>go(cur+1);
document.addEventListener('keydown',e=>{if(e.target.tagName==='BUTTON'&&e.key===' ')return;if(e.key==='ArrowRight')go(cur+1);if(e.key==='ArrowLeft')go(cur-1)});
go(0);
</script>
</body>
</html>
'''

html = PLANTILLA.replace("__TEXTO__", json.dumps(TEXTO_BASE, ensure_ascii=False)).replace("__CHAT__", json.dumps(CHAT, ensure_ascii=False))
DESTINO.parent.mkdir(parents=True, exist_ok=True)
DESTINO.write_text(html, encoding="utf-8")
print("Listo:", DESTINO, f"({len(html) // 1024} KB)")
