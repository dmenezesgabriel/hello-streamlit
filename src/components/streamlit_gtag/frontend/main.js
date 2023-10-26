class GtagHelper {
  static async setup(id) {
    const hasTagManager = [
      ...window.parent.document.head.querySelectorAll("script"),
    ]
      .map((el) => {
        return el.src.includes(id);
      })
      .some((el) => {
        return el === true;
      });
    if (hasTagManager) return;

    const ga = document.createElement("script");
    ga.async = true;
    ga.src = `https://www.googletagmanager.com/gtag/js?id=${id}`;

    window.parent.document.head.insertBefore(
      ga,
      window.parent.document.head.firstChild
    );

    const gtag = document.createElement("script");
    gtag.innerHTML = `
      window.dataLayer = window.dataLayer || [];

      function gtag() {
        dataLayer.push(arguments);
      }

      gtag("js", new Date());
      gtag("config", '${id}');

    `;
    window.parent.document.head.insertBefore(gtag, ga.nextSibling);
  }

  static async sendEvent(eventName, params) {
    window.parent.gtag("event", eventName, params);
    console.log(window.parent.dataLayer);
  }

  static async sendSet(params) {
    window.parent.gtag("set", params);
    console.log(window.parent.dataLayer);
  }
}

async function onRender(event) {
  const props = event.detail.args;
  await GtagHelper.setup(props.id);

  setTimeout(() => {
    console.log(window.parent.google_tag_manager);
    console.log(window.parent.google_tag_data);
  }, 1000);

  if (props.mode === "event") {
    await GtagHelper.sendEvent(props.mode, props.event_name, props.params);
  } else if (props.mode === "set") {
    await GtagHelper.sendSet(props.params);
  }
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender);
Streamlit.setComponentReady();
