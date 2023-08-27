import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"
import Plot from "react-plotly.js"

class PlotlyEvents extends StreamlitComponentBase {
  componentDidMount() {
    Streamlit.setFrameHeight(500)
  }

  public render = (): ReactNode => {
    const { data, layout, frames, config } = JSON.parse(this.props.args["spec"])
    return (
      <Plot
        data={data}
        layout={layout}
        frames={frames}
        config={config}
        onClick={this._onCLicked}
        onSelected={this._onSelected}
      />
    )
  }

  private _onCLicked = (eventData: Plotly.PlotMouseEvent): void => {
    const clickedPoints = eventData.points.map((point: Plotly.PlotDatum) => ({
      x: point.x,
      y: point.y,
    }))
    Streamlit.setComponentValue(clickedPoints)
  }

  private _onSelected = (eventData: Plotly.PlotSelectionEvent): void => {
    const clickedPoints = eventData.points.map((point: Plotly.PlotDatum) => ({
      x: point.x,
      y: point.y,
    }))
    Streamlit.setComponentValue(clickedPoints)
  }
}

export default withStreamlitConnection(PlotlyEvents)
