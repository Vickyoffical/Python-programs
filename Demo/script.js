const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const esc=t=>String(t).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
let tt;const toast=m=>{const t=$("#ts");t.textContent=m;t.classList.add("on");clearTimeout(tt);tt=setTimeout(()=>t.classList.remove("on"),2600)};
const go=id=>{$$(".scr").forEach(s=>s.classList.toggle("on",s.id===id));$$(".nv").forEach(b=>b.classList.toggle("on",b.dataset.go===id));scrollTo(0,0)};
$$("[data-go]").forEach(b=>b.onclick=()=>go(b.dataset.go));
document.addEventListener("click",e=>{const t=e.target.closest("[data-toast]");if(t)toast(t.dataset.toast)});
document.addEventListener("change",e=>{const t=e.target.closest("input[data-toast]");if(t)toast(t.dataset.toast)});
const hue=n=>[...n].reduce((a,c)=>a+c.charCodeAt(0),0)*47%360;
const av=n=>`<span class="av" style="background:hsl(${hue(n)} 45% 40%)">${esc(n[0])}</span>`;
let role="host",login=false;
const S={rooms:[["Friday movie night","Aarav",4,"Big Buck Bunny","Open"],["Hostel playlist","Isha",6,"Lo-fi mix","Approval"],["Docs club","Kabir",2,"Nothing playing","Approval"]],
 ppl:[["Aarav",true,-12],["Meera",false,38],["Kabir",false,-64],["Isha",false,121]],
 jr:["Dev","Sana"],rq:[["Kabir","Tears of Steel"],["Isha","Elephants Dream"]],q:["Big Buck Bunny","Sintel"],dur:[ "9:56","14:48"]};
$("#sw").onclick=()=>{login=!login;$("#dn").hidden=!login;$("#lt").textContent=$("#lb").textContent=login?"Create account":"Sign in";$("#sw").textContent=login?"I already have an account":"Create an account"};
$("#lf").onsubmit=e=>{e.preventDefault();toast("Signed in as "+esc($("#u").value));go("dash")};
$("#cf").onsubmit=e=>{e.preventDefault();const n=$("#rn").value.trim();if(!n)return toast("Enter a room name first.");$("#rt").textContent=n;S.rooms.unshift([n,"You",1,"Nothing playing","Approval"]);rooms();setRole("host");go("room");toast("Room created. Share the address and code.")};
function rooms(){$("#rooms").innerHTML=S.rooms.map((r,i)=>`<div class="room">${av(r[1])}<div><b>${esc(r[0])}</b><div class="mute" style="font-size:13px">Host ${esc(r[1])} &middot; ${r[2]} people &middot; ${esc(r[3])}</div></div><span class="pill sp">${r[4]=="Open"?"Open":"Needs approval"}</span><button class="btn sm ${r[4]=="Open"?"pri":""}" data-i="${i}">${r[4]=="Open"?"Join":"Ask to join"}</button></div>`).join("");
 $$("#rooms [data-i]").forEach(b=>b.onclick=()=>{const r=S.rooms[b.dataset.i];if(r[4]=="Open"){$("#rt").textContent=r[0];setRole("participant");go("room")}else toast("Request sent. "+r[1]+" will see it right away.")})}
function ppl(){const me=role=="host"?"Aarav":"Meera";$("#ppl").innerHTML=S.ppl.map(([n,h,d])=>{const w=Math.abs(d)>100;return `<div class="who">${av(n)}<div><b>${n}${n==me?" (you)":""}</b>${h?' <span class="pill">Host</span>':""}</div><div class="drift"><span class="trk" title="Offset from the host clock"><i class="${w?"w":""}" style="left:${50+d/3}%"></i></span>${d>0?"+":""}${d} ms</div>${role=="host"&&!h?`<button class="btn sm bad" data-rm="${n}">Remove</button>`:""}</div>`}).join("");
 $$("[data-rm]").forEach(b=>b.onclick=()=>{S.ppl=S.ppl.filter(p=>p[0]!=b.dataset.rm);ppl();toast(b.dataset.rm+" was removed from the room.")})}
function jr(){$("#jr").innerHTML=S.jr.length?S.jr.map(n=>`<div class="who">${av(n)}<b>${n}</b><span class="sp row"><button class="btn sm pri" data-a="${n}">Accept</button><button class="btn sm" data-x="${n}">Reject</button></span></div>`).join(""):'<p class="mute" style="margin:6px 0 0">No one is waiting. New requests appear here.</p>';
 $$("[data-a]").forEach(b=>b.onclick=()=>{S.jr=S.jr.filter(n=>n!=b.dataset.a);S.ppl.push([b.dataset.a,false,20]);jr();ppl();toast(b.dataset.a+" joined the room.")});
 $$("[data-x]").forEach(b=>b.onclick=()=>{S.jr=S.jr.filter(n=>n!=b.dataset.x);jr();toast("Request from "+b.dataset.x+" rejected.")})}
function rq(){const h=role=="host";$("#rqt").textContent=h?"Media requests":"Your requests";const L=h?S.rq:S.rq.filter(r=>r[0]=="Isha");
 $("#rqs").innerHTML=L.length?L.map(r=>`<div class="who">${av(r[0])}<div><b>${esc(r[1])}</b><div class="mute" style="font-size:13px">from ${esc(r[0])}</div></div>${h?`<span class="sp row"><button class="btn sm pri" data-ra="${esc(r[1])}">Add to queue</button><button class="btn sm" data-rx="${esc(r[1])}">Reject</button></span>`:'<span class="pill warn sp">Waiting for host</span>'}</div>`).join(""):'<p class="mute" style="margin:6px 0 0">No requests yet.</p>';
 $$("[data-ra]").forEach(b=>b.onclick=()=>{S.rq=S.rq.filter(r=>r[1]!=b.dataset.ra);S.q.push(b.dataset.ra);S.dur.push("--:--");rq();queue();toast("Added to the queue.")});
 $$("[data-rx]").forEach(b=>b.onclick=()=>{S.rq=S.rq.filter(r=>r[1]!=b.dataset.rx);rq();toast("Request rejected.")})}
function queue(){$("#qc").textContent=S.q.length+" in queue";$("#queue").innerHTML=S.q.map((t,i)=>`<div class="q"><b>${esc(t)}</b>${i==0?'<span class="pill ok">Playing</span>':""}<span class="mute" style="font-size:13px">${S.dur[i]}</span><span class="sp row hostonly">${i?`<button class="btn sm" data-pn="${i}">Play now</button>`:""}<button class="btn sm bad" data-d="${i}">Remove</button></span></div>`).join("");
 $$("[data-d]").forEach(b=>b.onclick=()=>{S.q.splice(b.dataset.d,1);S.dur.splice(b.dataset.d,1);queue();toast("Removed from the queue.")});
 $$("[data-pn]").forEach(b=>b.onclick=()=>{const i=+b.dataset.pn;S.q.unshift(...S.q.splice(i,1));S.dur.unshift(...S.dur.splice(i,1));queue();$(".stage b").textContent=S.q[0];pos=0;toast("Now playing "+S.q[0]+" for everyone.")})}
$("#rb").onclick=()=>{const v=$("#rq").value.trim();if(!v)return toast("Type a title to request.");S.rq.push([role=="host"?"Aarav":"Isha",v]);$("#rq").value="";rq();toast("Request sent to the host.")};
function setRole(r){role=r;document.body.dataset.role=r;$$("#seg button").forEach(b=>b.classList.toggle("on",b.dataset.r==r));$("#rp").textContent=r=="host"?"You are the host":"You are a participant";
 $("#sk").disabled=r!="host";$("#sk").title=r!="host"?"Only the host can seek":"";$("#pn").textContent=r=="host"?"Pausing pauses the room for everyone, so nobody misses a scene.":"You can pause and play for everyone. Only the host can seek or stop.";ppl();jr();rq();queue()}
$$("#seg button").forEach(b=>b.onclick=()=>setRole(b.dataset.r));
let pos=125.42,playing=true;const f=s=>Math.floor(s/60)+":"+String(Math.floor(s%60)).padStart(2,"0");
function draw(){$("#sk").value=pos;$("#tm").textContent=f(pos)+" / 9:56";$("#pp").innerHTML=playing?"&#10074;&#10074;":"&#9654;"}
$("#pp").onclick=()=>{playing=!playing;draw();toast(playing?"Playing for everyone.":"Paused for everyone.")};
$("#st").onclick=()=>{playing=false;pos=0;draw();toast("Stopped. The room is back at the start.")};
$("#sk").oninput=e=>{pos=+e.target.value;draw()};
$("#sk").onchange=()=>toast("Everyone jumped to "+f(pos)+".");
setInterval(()=>{if(playing){pos=Math.min(596,pos+.25);draw()}},250);
setInterval(()=>{if(!playing)return;S.ppl.forEach(p=>{if(!p[1])p[2]=Math.max(-140,Math.min(140,p[2]+Math.round((Math.random()-.5)*50)))});
 const m=S.ppl.find(p=>p[0]==(role=="host"?"Aarav":"Meera"));$("#sy").textContent="Synced \u00b7 "+Math.abs(m[2])+" ms";ppl()},2200);
rooms();setRole("host");draw();
