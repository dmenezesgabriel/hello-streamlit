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
      gtag("config", id);
    `;
    window.parent.document.head.insertBefore(gtag, ga.nextSibling);
  }

  static async sendEvent(eventName, params) {
    window.dataLayer = window.dataLayer || [];
    function gtag() {
      dataLayer.push(arguments);
    }
    gtag("event", eventName, params);
  }

  static async sendSet(params) {
    window.dataLayer = window.dataLayer || [];
    function gtag() {
      dataLayer.push(arguments);
    }
    gtag("set", params);
  }
}

async function onRender(event) {
  const props = event.detail.args;
  console.log(props);

  await GtagHelper.setup(props.id);

  if (props.mode === "event") {
    await GtagHelper.sendEvent(props.mode, props.event_name, props.params);
  } else if (props.mode === "set") {
    await GtagHelper.sendSet(props.params);
  }
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender);
Streamlit.setComponentReady();
