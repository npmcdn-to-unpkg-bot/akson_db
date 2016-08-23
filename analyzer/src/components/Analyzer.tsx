import * as React from "react";

import DataViewer from "./DataViewer";
import AnalyzerNavbar from "./AnalyzerNavbar";


export interface AnalyzerState {
  currentChartId?: number;
  currentPatientId?: number;
}

export class Analyzer extends React.Component<any, AnalyzerState> {

  private newChart = (patientId: number) => {
    this.setState({
      currentPatientId: patientId,
      currentChartId: null
    })
  };

  private selectChart = (patientId: number, chartId: number): void => {
    this.setState({
      currentPatientId: patientId,
      currentChartId: chartId
    });
  };

  render() {
    return (
      <div>
        <DataViewer {...this.state}/>
        <AnalyzerNavbar
          newChart={this.newChart}
          selectChart={this.selectChart}
        />
      </div>
    );
  }
}
