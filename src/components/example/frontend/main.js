class InputComponent {
  constructor() {
    this.textInput = document.getElementById("text_input");
    this.textInput.addEventListener("input", this.inputHandler.bind(this));
    Streamlit.setFrameHeight(200);
  }

  inputHandler() {
    Streamlit.setComponentValue(this.textInput.value);
  }

  setValue(value) {
    if (this.textInput.value === "") {
      this.textInput.value = value;
    }
  }
}

function onRender(event) {
  const props = event.detail.args;

  const inputComponent = new InputComponent();
  inputComponent.setValue(props.initial_state.message);
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender);
Streamlit.setComponentReady();
