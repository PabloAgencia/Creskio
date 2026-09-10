(function () {
  var cfg = Object.assign({
    businessName: "Creskio",
    whatsappNumber: "",
    primaryColor: "#8b5cf6",
    avatarEmoji: "🤖",
    greeting: "¡Hola! ¿En qué te puedo ayudar?",
    initialQuickReplies: [],
    launcherBottom: "30px",
    windowBottom: "110px",
    launcherLeft: "30px",
    apiUrl: "/api/chat"
  }, window.CRESKIO_WIDGET_CONFIG || {});

  var viewportMeta = document.querySelector('meta[name="viewport"]');
  if (viewportMeta) {
    if (viewportMeta.content.indexOf('viewport-fit') === -1) {
      viewportMeta.content = viewportMeta.content.replace(/\s*$/, '') + ', viewport-fit=cover';
    }
  } else {
    viewportMeta = document.createElement('meta');
    viewportMeta.name = 'viewport';
    viewportMeta.content = 'width=device-width, initial-scale=1, viewport-fit=cover';
    document.head.appendChild(viewportMeta);
  }

  var prevHost = document.getElementById('creskio-widget-host');
  if (prevHost) prevHost.remove();

  var host = document.createElement('div');
  host.id = 'creskio-widget-host';
  document.body.appendChild(host);
  var root = host.attachShadow({ mode: 'open' });

  function shade(hex, percent) {
    var h = String(hex).replace('#', '');
    var full = h.length === 3 ? h.split('').map(function (c) { return c + c; }).join('') : h;
    var num = parseInt(full, 16);
    var adj = Math.round(255 * percent / 100);
    var r = Math.min(255, Math.max(0, (num >> 16) + adj));
    var g = Math.min(255, Math.max(0, ((num >> 8) & 0xFF) + adj));
    var b = Math.min(255, Math.max(0, (num & 0xFF) + adj));
    return '#' + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
  }

  var primaryDark = shade(cfg.primaryColor, -14);

  var css = `
  * { box-sizing: border-box; margin: 0; padding: 0; cursor: auto; }
  :host {
    --cb-primary: ${cfg.primaryColor};
    --cb-primary-dark: ${primaryDark};
    --cb-on-primary: #ffffff;
    --cb-bg: #0d0b14;
    --cb-text-muted: #9a93a8;
    --cb-shadow: 0 16px 56px rgba(0,0,0,.5), 0 0 0 1px rgba(139,92,246,.18);
    --cb-radius: 16px;
    --cb-wa-green: #25D366;
    --cb-charcoal: #16121f;
    --cb-primary-soft: rgba(139,92,246,.15);
  }
  button { font: inherit; cursor: pointer; }
  input { cursor: text; }
  .cb-launcher {
    all: unset;
    box-sizing: border-box;
    position: fixed; bottom: calc(${cfg.launcherBottom} + env(safe-area-inset-bottom, 0px)); left: calc(${cfg.launcherLeft} + env(safe-area-inset-left, 0px)); right: auto;
    width: 64px; height: 64px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--cb-primary), var(--cb-primary-dark));
    color: var(--cb-on-primary);
    cursor: pointer;
    box-shadow: 0 6px 24px rgba(139,92,246,.45);
    display: flex; align-items: center; justify-content: center;
    z-index: 999998;
    transition: transform .3s ease, box-shadow .3s ease;
    animation: cb-pulse 3s infinite;
    font-family: system-ui, sans-serif;
  }
  @keyframes cb-pulse {
    0%, 100% { box-shadow: 0 0 0 0 rgba(139,92,246,.4); }
    50%      { box-shadow: 0 0 0 12px rgba(139,92,246,0); }
  }
  .cb-launcher:hover { transform: scale(1.08); box-shadow: 0 8px 32px rgba(139,92,246,.6); }
  .cb-launcher:active { transform: scale(.96); }
  .cb-launcher svg { width: 28px; height: 28px; flex-shrink: 0; }
  .cb-launcher.is-open { transform: scale(0); pointer-events: none; }
  .cb-hint-badge {
    position: fixed;
    bottom: calc(${cfg.launcherBottom} + 44px + env(safe-area-inset-bottom, 0px));
    left: calc(${cfg.launcherLeft} + 44px + env(safe-area-inset-left, 0px));
    width: 20px; height: 20px;
    background: #ef4444; border-radius: 50%;
    color: #fff; font-size: 11px; font-weight: 700;
    font-family: system-ui, sans-serif;
    display: flex; align-items: center; justify-content: center;
    opacity: 0; transform: scale(0);
    transition: opacity .3s, transform .3s;
    pointer-events: none; z-index: 999998;
  }
  .cb-hint-badge.show { opacity: 1; transform: scale(1); animation: cb-badge-pop .4s cubic-bezier(.34,1.56,.64,1); }
  @keyframes cb-badge-pop { from{transform:scale(0)} 60%{transform:scale(1.3)} to{transform:scale(1)} }
  .cb-hint-tip {
    position: fixed;
    bottom: calc(${cfg.launcherBottom} + 22px + env(safe-area-inset-bottom, 0px));
    left: calc(${cfg.launcherLeft} + 76px + env(safe-area-inset-left, 0px));
    background: var(--cb-charcoal); color: #fff;
    font-family: system-ui, sans-serif; font-size: 12.5px; font-weight: 600;
    padding: 8px 14px; white-space: nowrap;
    border: 1px solid rgba(139,92,246,.35); border-radius: 10px;
    box-shadow: 0 4px 16px rgba(0,0,0,.4);
    opacity: 0; transition: opacity .35s; pointer-events: none; z-index: 999998;
  }
  .cb-hint-tip.show { opacity: 1; }
  .cb-window {
    all: unset;
    box-sizing: border-box;
    position: fixed; bottom: calc(${cfg.windowBottom} + env(safe-area-inset-bottom, 0px)); left: calc(${cfg.launcherLeft} + env(safe-area-inset-left, 0px)); right: auto;
    width: 370px; max-width: calc(100vw - 60px);
    height: 560px; max-height: calc(100vh - 140px);
    background: var(--cb-bg);
    border-radius: var(--cb-radius);
    box-shadow: var(--cb-shadow);
    display: flex; flex-direction: column;
    overflow: hidden;
    z-index: 999999;
    transform: translateY(20px) scale(.94); opacity: 0; pointer-events: none;
    transform-origin: bottom left;
    transition: transform .3s cubic-bezier(.34,1.56,.64,1), opacity .25s ease;
    font-family: system-ui, sans-serif;
  }
  .cb-window.is-open { transform: translateY(0) scale(1); opacity: 1; pointer-events: auto; }
  .cb-header { box-sizing: border-box; width: 100%; background: var(--cb-charcoal); color: #fff; padding: 16px 14px; display: flex; align-items: center; gap: 12px; border-bottom: 2px solid var(--cb-primary); flex-shrink: 0; }
  .cb-avatar { box-sizing: border-box; width: 42px; height: 42px; border-radius: 50%; background: var(--cb-primary-soft); border: 1px solid rgba(139,92,246,.4); display: flex; align-items: center; justify-content: center; font-size: 20px; flex-shrink: 0; color: var(--cb-primary); }
  .cb-header-text { flex: 1; min-width: 0; }
  .cb-header-name { font-weight: 700; font-size: 15px; line-height: 1.2; color: #fff; white-space: normal; }
  .cb-header-status { font-size: 10px; opacity: .9; color: var(--cb-primary); text-transform: uppercase; letter-spacing: .1em; display: flex; align-items: center; gap: 6px; margin-top: 4px; font-weight: 500; }
  .cb-header-status::before { content: ''; width: 7px; height: 7px; background: #4ade80; border-radius: 50%; box-shadow: 0 0 0 2px rgba(74,222,128,.3); flex-shrink: 0; }
  .cb-header-actions { display: flex; gap: 6px; flex-shrink: 0; }
  .cb-header-btn { all: unset; box-sizing: border-box; background: rgba(255,255,255,.10); width: 34px; height: 34px; border-radius: 50%; color: #fff; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: background .2s ease; flex-shrink: 0; }
  .cb-header-btn:hover { background: rgba(255,255,255,.22); }
  .cb-header-btn svg { width: 18px; height: 18px; flex-shrink: 0; }
  .cb-header-btn.cb-wa { background: var(--cb-wa-green); }
  .cb-header-btn.cb-wa:hover { background: #1ebe57; }
  .cb-messages { box-sizing: border-box; width: 100%; flex: 1; overflow-y: auto; padding: 16px 14px; display: flex; flex-direction: column; gap: 10px; background: var(--cb-bg); background-image: radial-gradient(ellipse 80% 80% at 50% 50%, rgba(139,92,246,.06) 0%, transparent 100%); }
  .cb-messages::-webkit-scrollbar { width: 4px; }
  .cb-messages::-webkit-scrollbar-thumb { background: var(--cb-primary); border-radius: 2px; }
  .cb-messages::-webkit-scrollbar-track { background: transparent; }
  .cb-msg { box-sizing: border-box; max-width: 85%; padding: 11px 15px; border-radius: 14px; font-size: 14.5px; line-height: 1.5; animation: cb-msg-in .25s ease; word-wrap: break-word; white-space: pre-wrap; font-weight: 400; }
  @keyframes cb-msg-in { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
  .cb-msg.cb-bot { background: #1c1826; color: #e8e5ef; align-self: flex-start; border: 1px solid rgba(139,92,246,.20); border-bottom-left-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,.15); }
  .cb-msg.cb-user { background: linear-gradient(135deg, var(--cb-primary), var(--cb-primary-dark)); color: var(--cb-on-primary); align-self: flex-end; border-bottom-right-radius: 4px; font-weight: 500; }
  .cb-quick-replies { display: flex; flex-wrap: wrap; gap: 6px; align-self: flex-start; max-width: 100%; margin-top: 2px; }
  .cb-qr-btn { all: unset; box-sizing: border-box; background: #1c1826; color: #cfc8de; border: 1px solid var(--cb-primary); padding: 7px 13px; border-radius: 50px; font-size: 12.5px; font-weight: 500; letter-spacing: .01em; cursor: pointer; transition: all .2s ease; }
  .cb-qr-btn:hover { background: var(--cb-primary); color: #fff; transform: translateY(-1px); box-shadow: 0 4px 12px rgba(139,92,246,.35); }
  .cb-qr-btn.cb-qr-wa { background: var(--cb-wa-green); color: #fff; border-color: var(--cb-wa-green); }
  .cb-qr-btn.cb-qr-wa:hover { background: #1ebe57; border-color: #1ebe57; }
  .cb-typing { align-self: flex-start; background: #1c1826; border: 1px solid rgba(139,92,246,.20); border-radius: 14px; border-bottom-left-radius: 4px; padding: 12px 16px; display: flex; gap: 4px; }
  .cb-typing span { width: 6px; height: 6px; background: var(--cb-primary); border-radius: 50%; animation: cb-bounce 1.4s infinite ease-in-out both; }
  .cb-typing span:nth-child(1) { animation-delay: -.32s; }
  .cb-typing span:nth-child(2) { animation-delay: -.16s; }
  @keyframes cb-bounce { 0%, 80%, 100% { transform: scale(0); opacity: .5; } 40% { transform: scale(1); opacity: 1; } }
  .cb-input-bar { box-sizing: border-box; width: 100%; padding: 12px 14px; background: var(--cb-charcoal); border-top: 1px solid rgba(139,92,246,.18); display: flex; gap: 8px; align-items: center; flex-shrink: 0; }
  .cb-input { all: unset; box-sizing: border-box; flex: 1; border: 1px solid rgba(139,92,246,.30); background: #0d0b14; border-radius: 50px; padding: 11px 16px; font-size: 14px; color: #fff; font-family: inherit; transition: border-color .25s, box-shadow .25s; }
  .cb-input::placeholder { color: var(--cb-text-muted); opacity: .8; }
  .cb-input:focus { border-color: var(--cb-primary); box-shadow: 0 0 0 2px rgba(139,92,246,.2); }
  .cb-send { all: unset; box-sizing: border-box; width: 42px; height: 42px; border-radius: 50%; background: linear-gradient(135deg, var(--cb-primary), var(--cb-primary-dark)); color: #fff; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: transform .15s; flex-shrink: 0; }
  .cb-send:hover { transform: scale(1.06); }
  .cb-send:active { transform: scale(.94); }
  .cb-send svg { width: 18px; height: 18px; flex-shrink: 0; }
  .cb-disclaimer { box-sizing: border-box; width: 100%; font-size: 10.5px; color: var(--cb-text-muted); text-align: center; padding: 6px 14px 9px; background: var(--cb-charcoal); letter-spacing: .02em; flex-shrink: 0; }
  a { color: var(--cb-primary); }
  @media (max-width: 768px) {
    .cb-launcher { bottom: calc(90px + env(safe-area-inset-bottom, 0px)); left: calc(16px + env(safe-area-inset-left, 0px)); width: 58px; height: 58px; }
    .cb-window { bottom: calc(90px + env(safe-area-inset-bottom, 0px)); left: calc(16px + env(safe-area-inset-left, 0px)); width: calc(100vw - 32px); height: 480px; max-height: calc(100vh - 110px); }
    .cb-hint-badge { bottom: calc(90px + 38px + env(safe-area-inset-bottom, 0px)); left: calc(16px + 38px + env(safe-area-inset-left, 0px)); }
    .cb-hint-tip { display: none; }
  }
  @media (max-width: 420px) {
    .cb-window { width: calc(100vw - 24px); left: calc(12px + env(safe-area-inset-left, 0px)); height: calc(100vh - 110px); max-height: calc(100vh - 110px); }
    .cb-launcher { left: calc(12px + env(safe-area-inset-left, 0px)); }
  }
  `;
  var style = document.createElement('style');
  style.textContent = css;
  root.appendChild(style);

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function buildWhatsAppUrl(prefillText) {
    var text = encodeURIComponent(prefillText || ('Hola, vengo de la web de ' + cfg.businessName + '.'));
    return 'https://wa.me/' + cfg.whatsappNumber + '?text=' + text;
  }
  function openWhatsApp(prefillText) {
    window.open(buildWhatsAppUrl(prefillText), '_blank', 'noopener');
  }

  var launcher, win, msgsEl, inputEl, sendBtn, hintBadge, hintTip, isOpen = false;

  function buildDOM() {
    launcher = document.createElement('button');
    launcher.className = 'cb-launcher';
    launcher.setAttribute('aria-label', 'Abrir chat');
    launcher.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>';
    launcher.addEventListener('click', toggleOpen);

    win = document.createElement('div');
    win.className = 'cb-window';
    win.setAttribute('role', 'dialog');
    win.setAttribute('aria-label', 'Chat con ' + cfg.businessName);
    win.innerHTML =
      '<div class="cb-header">' +
      '  <div class="cb-avatar">' + escapeHtml(cfg.avatarEmoji) + '</div>' +
      '  <div class="cb-header-text">' +
      '    <div class="cb-header-name">' + escapeHtml(cfg.businessName) + '</div>' +
      '    <div class="cb-header-status">En línea</div>' +
      '  </div>' +
      '  <div class="cb-header-actions">' +
      '    <button class="cb-header-btn cb-wa" aria-label="Hablar con humano por WhatsApp" title="Hablar con Pablo"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.6 6.3A7.85 7.85 0 0 0 12 4a7.94 7.94 0 0 0-6.8 12L4 20l4.1-1.1A7.94 7.94 0 0 0 20 12c0-2.1-.85-4.1-2.4-5.7zM12 18.5a6.4 6.4 0 0 1-3.3-.9l-.24-.14-2.43.65.65-2.37-.16-.25A6.55 6.55 0 1 1 12 18.5zm3.6-4.9c-.2-.1-1.16-.57-1.34-.64s-.31-.1-.44.1-.5.64-.62.78-.23.15-.43.05a5.4 5.4 0 0 1-1.59-.98 5.94 5.94 0 0 1-1.1-1.36c-.11-.2 0-.3.09-.4l.3-.34c.1-.12.13-.2.2-.34s.04-.25 0-.35-.43-1.05-.6-1.43-.32-.32-.43-.33h-.37a.7.7 0 0 0-.5.24 2.13 2.13 0 0 0-.66 1.58 3.7 3.7 0 0 0 .77 1.95c.1.13 1.34 2.05 3.25 2.87a3.42 3.42 0 0 0 2.18.45 1.96 1.96 0 0 0 1.3-.92 1.6 1.6 0 0 0 .12-.92c-.05-.08-.18-.13-.38-.23z"/></svg></button>' +
      '    <button class="cb-header-btn cb-close" aria-label="Cerrar chat" title="Cerrar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button>' +
      '  </div>' +
      '</div>' +
      '<div class="cb-messages" aria-live="polite"></div>' +
      '<div class="cb-input-bar">' +
      '  <input type="text" class="cb-input" placeholder="Escribe tu consulta..." aria-label="Mensaje" maxlength="500" autocomplete="off">' +
      '  <button class="cb-send" aria-label="Enviar"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M2 21l21-9L2 3v7l15 2-15 2z"/></svg></button>' +
      '</div>' +
      '<div class="cb-disclaimer">Agente IA de Creskio · Demo en vivo</div>';

    hintBadge = document.createElement('div');
    hintBadge.className = 'cb-hint-badge';
    hintBadge.textContent = '1';

    hintTip = document.createElement('div');
    hintTip.className = 'cb-hint-tip';
    hintTip.textContent = '¿Alguna duda? ¡Pregúntame! 💬';

    root.appendChild(launcher);
    root.appendChild(win);
    root.appendChild(hintBadge);
    root.appendChild(hintTip);

    msgsEl = win.querySelector('.cb-messages');
    inputEl = win.querySelector('.cb-input');
    sendBtn = win.querySelector('.cb-send');

    win.querySelector('.cb-close').addEventListener('click', toggleOpen);
    win.querySelector('.cb-wa').addEventListener('click', function () { openWhatsApp(); });
    sendBtn.addEventListener('click', onSend);
    inputEl.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') { e.preventDefault(); onSend(); }
    });
    root.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isOpen) toggleOpen();
    });
  }

  function toggleOpen() {
    isOpen = !isOpen;
    win.classList.toggle('is-open', isOpen);
    launcher.classList.toggle('is-open', isOpen);
    if (isOpen) {
      hintBadge.classList.remove('show');
      hintTip.classList.remove('show');
      if (!msgsEl.children.length) showGreeting();
      setTimeout(function () { inputEl.focus(); }, 250);
    }
  }
  function showGreeting() {
    addBotMessage(cfg.greeting, cfg.initialQuickReplies);
  }
  function addBotMessage(text, quickReplies) {
    showTyping();
    setTimeout(function () {
      removeTyping();
      var bubble = document.createElement('div');
      bubble.className = 'cb-msg cb-bot';
      bubble.textContent = text;
      msgsEl.appendChild(bubble);
      if (quickReplies && quickReplies.length) {
        var qrWrap = document.createElement('div');
        qrWrap.className = 'cb-quick-replies';
        quickReplies.forEach(function (qr) {
          var btn = document.createElement('button');
          btn.className = 'cb-qr-btn' + (qr.action === 'whatsapp' ? ' cb-qr-wa' : '');
          btn.textContent = qr.label;
          btn.addEventListener('click', function () {
            if (qr.action === 'whatsapp') openWhatsApp(qr.prefill);
            else if (qr.send) { inputEl.value = qr.send; onSend(); }
          });
          qrWrap.appendChild(btn);
        });
        msgsEl.appendChild(qrWrap);
      }
      scrollToBottom();
    }, 480);
  }
  function addUserMessage(text) {
    var bubble = document.createElement('div');
    bubble.className = 'cb-msg cb-user';
    bubble.textContent = text;
    msgsEl.appendChild(bubble);
    scrollToBottom();
  }
  function showTyping() {
    removeTyping();
    var t = document.createElement('div');
    t.className = 'cb-typing';
    t.setAttribute('data-typing', '1');
    t.innerHTML = '<span></span><span></span><span></span>';
    msgsEl.appendChild(t);
    scrollToBottom();
  }
  function removeTyping() {
    var t = msgsEl.querySelector('[data-typing]');
    if (t) t.remove();
  }
  function scrollToBottom() { msgsEl.scrollTop = msgsEl.scrollHeight; }

  var conversationHistory = [];
  var sessionId = 'creskio-' + Math.random().toString(36).slice(2) + Date.now().toString(36);

  function linkify(text) {
    var e = text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    return e.replace(/(https?:\/\/[^\s<>"']+)/g, function (u) {
      if (u.indexOf('wa.me') !== -1) return '<a href="' + u + '" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:4px;background:#25D366;color:#fff;padding:3px 10px;border-radius:20px;text-decoration:none;font-size:.85em;font-weight:700;">💬 WhatsApp</a>';
      return '<a href="' + u + '" target="_blank" rel="noopener" style="color:var(--cb-primary);text-decoration:underline;word-break:break-all;">' + u + '</a>';
    });
  }

  async function onSend() {
    var text = inputEl.value.trim();
    if (!text) return;
    inputEl.value = '';
    sendBtn.disabled = true;
    addUserMessage(text);
    conversationHistory.push({ role: 'user', content: text });
    showTyping();
    try {
      var res = await fetch(cfg.apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages: conversationHistory, sessionId: sessionId })
      });
      var data = await res.json();
      removeTyping();
      var reply = data.reply || 'Lo siento, hubo un problema.';
      conversationHistory.push({ role: 'assistant', content: reply });
      var bubble = document.createElement('div');
      bubble.className = 'cb-msg cb-bot';
      bubble.innerHTML = linkify(reply);
      msgsEl.appendChild(bubble);
      scrollToBottom();
    } catch (err) {
      removeTyping();
      var bubble2 = document.createElement('div');
      bubble2.className = 'cb-msg cb-bot';
      bubble2.textContent = 'Lo siento, hubo un problema.';
      msgsEl.appendChild(bubble2);
      scrollToBottom();
    } finally {
      sendBtn.disabled = false;
    }
  }

  buildDOM();

  (function () {
    var seenKey = 'creskio_hint_seen';
    if (sessionStorage.getItem(seenKey)) return;
    setTimeout(function () {
      if (sessionStorage.getItem(seenKey) || isOpen) return;
      sessionStorage.setItem(seenKey, '1');
      hintBadge.classList.add('show');
      hintTip.classList.add('show');
    }, 3000);
  })();

  window.CreskioChatbot = {
    open: function () { if (!isOpen) toggleOpen(); },
    close: function () { if (isOpen) toggleOpen(); }
  };
})();
