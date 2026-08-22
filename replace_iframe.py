import os

base_dir = "/Users/jadewee/Desktop/Obrig/outpost-website"
microsites = ['crawford.html', 'changi.html', 'clementi.html']

user_snippet = """<iframe
  id="rezerv-widget-iframe"
  src="https://widgets.rezerv.co/timetable?businessId=c8961b16-cd44-466f-8882-8b41fdb535d4&businessUrl=https%3A%2F%2Foutpostclimbing.sg&fontFamily=Roboto&gaEnabled=false&gaId=&hideBranding=false&layout=list&noClassDisplay=12&openInNewTab=true&outlinedButtonColor=%23010101&primaryBackground=%23ECE5D7&scheduleTabs=%5B%7B%22id%22%3A%22classes%22%2C%22label%22%3A%22Classes%22%2C%22source%22%3A%22classes%22%2C%22visible%22%3Atrue%7D%2C%7B%22id%22%3A%22appointments%22%2C%22label%22%3A%22Appointments%22%2C%22source%22%3A%22appointments%22%2C%22visible%22%3Afalse%7D%5D&scheduleViewType=list&scheduleViewTypeOrder=%5B%22list%22%2C%22grid%22%5D&scheduleViewTypeVisibility=%7B%22list%22%3Atrue%2C%22grid%22%3Atrue%7D&secondaryBackground=%23FFFFFF&showRatings=false&showSlotsLeft=false&showSwitcherTabs=true&solidButtonBackground=%23000000&solidButtonText=%23FFFFFF&subCategory=Show+all&textColor=%23000000"
  frameborder="0"
  style="border: none; width: 100%; height: 1080px; border-radius: 20px;"
  data-hide-branding="false"
  data-show-ratings="false"
></iframe>
<script>
(function () {
  var IFRAME_SELECTOR = '#rezerv-widget-iframe';
  var WIDGET_ORIGIN = 'https://widgets.rezerv.co';
  var UTM_REQUEST_MESSAGE_TYPE = 'REQUEST_UTM_PARAMS';
  var UTM_KEYS = ['utm_source', 'utm_campaign', 'utm_medium', 'utm_term', 'utm_content'];
  function collectUtms() {
    var params = new URLSearchParams(window.location.search);
    var utms = {};
    UTM_KEYS.forEach(function (key) {
      var value = params.get(key);
      if (value) utms[key] = value;
    });
    return utms;
  }
  function postUtmsToWidget(iframe, utms) {
    if (!iframe || !iframe.contentWindow || Object.keys(utms).length === 0) return;
    iframe.contentWindow.postMessage({ type: 'UTM_PARAMS', utms: utms }, WIDGET_ORIGIN);
  }
  function init() {
    var iframe = document.querySelector(IFRAME_SELECTOR);
    if (!iframe) return;
    function sendUtms() {
      postUtmsToWidget(iframe, collectUtms());
    }
    iframe.addEventListener('load', function () {
      sendUtms();
      setTimeout(sendUtms, 500);
      setTimeout(sendUtms, 1500);
    });
    window.addEventListener('message', function (event) {
      if (event.origin !== WIDGET_ORIGIN) return;
      if (event.data && event.data.type === UTM_REQUEST_MESSAGE_TYPE) {
        sendUtms();
      }
    });
    sendUtms();
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>"""

old_snippet = '''<!-- REPLACE THE SRC ATTRIBUTE BELOW WITH YOUR ACTUAL REZERV IFRAME URL -->
      <iframe src="https://example.rezerv.co/widget" width="100%" height="600" frameborder="0" style="border:0; border-radius: 20px;" allowfullscreen></iframe>'''

for site in microsites:
    path = os.path.join(base_dir, site)
    with open(path, 'r') as f:
        content = f.read()
    
    if old_snippet in content:
        new_content = content.replace(old_snippet, user_snippet)
        with open(path, 'w') as f:
            f.write(new_content)

print("Replaced placeholder with user snippet.")
