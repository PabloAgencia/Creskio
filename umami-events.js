/* Eventos de Umami (analítica sin cookies). Si Umami no carga, no pasa nada. */
(function () {
  function t(name, data) { try { if (window.umami) window.umami.track(name, data); } catch (e) {} }
  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a,button') : null;
    if (!a) return;
    var href = a.getAttribute('href') || '';
    if (/wa\.me|api\.whatsapp\.com/.test(href)) t('whatsapp_click', { pagina: location.pathname });
    else if (a.id === 'demoOpen' || a.classList.contains('demoOpenBtn')) t('demo_tienda_abrir', { pagina: location.pathname });
    else if (a.id === 'demoGo') t('demo_tienda_ir');
    else if (a.id === 'demoCopy') t('demo_tienda_copiar_clave');
    else if (/tienda-online/.test(href)) t('ver_tienda_online', { desde: location.pathname });
    else if (/cal\.com/.test(href)) t('reserva_click');
    else if (a.className && /cb-launcher|cb-toggle|chat-launcher/.test(a.className)) t('chat_abrir');
  }, true);
  var v = document.querySelector('video[controls], .lp-hvid');
  if (v) v.addEventListener('play', function () { t('video_tienda_play'); }, { once: true });
})();
