import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import { ReactNode } from "react"
import Plot from "react-plotly.js"

class PlotlyEvents extends StreamlitComponentBase {
  componentDidMount() {
    Streamlit.setFrameHeight(500)
  }

  public render = (): ReactNode => {
    const { data, layout, frames, config } = JSON.parse(this.props.args["fig"])
    const clickEvent = this.props.args["click_event"]
    const selectEvent = this.props.args["select_event"]
    const hoverEvent = this.props.args["hover_event"]
    const doubleClickEvent = this.props.args["double_click_event"]
    const overrideHeight = this.props.args["override_height"]
    const overrideWidth = this.props.args["override_width"]

    return (
      <Plot
        data={data}
        layout={layout}
        frames={frames}
        config={config}
        onClick={clickEvent ? this._onCLicked : function () {}}
        onSelected={selectEvent ? this._onSelected : function () {}}
        onHover={hoverEvent ? this._onHover : function () {}}
        onDoubleClick={doubleClickEvent ? this._onDoubleClick : function () {}}
        style={{ width: overrideWidth, height: overrideHeight }}
        className="stPlotlyChart"
      />
    )
  }
  private _extractEventData = (eventData: Plotly.PlotDatum[]): any[] => {
    return eventData.map((point: Plotly.PlotDatum) => ({
      x: point.x,
      y: point.y,
    }))
  }

  private _onCLicked = (eventData: Plotly.PlotMouseEvent): void => {
    const clickedPoints = this._extractEventData(eventData.points)
    Streamlit.setComponentValue(clickedPoints)
  }

  private _onSelected = (eventData: Plotly.PlotSelectionEvent): void => {
    const clickedPoints = this._extractEventData(eventData.points)
    if (clickedPoints.length === 0) {
      return
    }
    Streamlit.setComponentValue(clickedPoints)
  }

  private _onHover = (eventData: Plotly.PlotHoverEvent): void => {
    const clickedPoints = this._extractEventData(eventData.points)
    Streamlit.setComponentValue(clickedPoints)
  }

  private _onDoubleClick = (): void => {
    // const { data } = JSON.parse(this.props.args["fig"])
    Streamlit.setComponentValue([])
  }
}

export default withStreamlitConnection(PlotlyEvents)
