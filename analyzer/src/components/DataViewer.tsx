import * as React from "react";
import * as $ from "jquery";
import NeurorehabilitationProperties from "./NeurorehabilitationProperties";
import Chart from "./Chart";


export interface DataViewerProps {
  currentPatientId?: number;
  currentChartId?: number;
}

export interface DataViewerState {
  chartsData: any;
}


export default class AnalyzerCharts extends React.Component<DataViewerProps, DataViewerState> {

  private updateCharts = (data: any[]) => {
    this.setState({
      chartsData: data
    })
  };

  private renderProperties = () => {
    if (this.props.currentPatientId) {
      return (
        <NeurorehabilitationProperties {...this.props} updateCharts={this.updateCharts}/>
      );
    }
    return (
      <div>
        Akson analyzer tool
      </div>
    )
  }

  private renderCharts = (): any => {

    return null;
  }

  render() {
    return (
      <div id="viewer">
        {this.renderProperties()}
        {this.renderCharts()}
      </div>
    );
  }
}
