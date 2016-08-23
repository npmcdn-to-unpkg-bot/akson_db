import * as React from "react";


export interface ChartProps {
  currentChartId?: number;
  chartsParameters?: any[];
}

export default class Chart extends React.Component<ChartProps, {}> {
  getChart = () => {
    if (this.props.currentChartId)
      $.get("./api/neurorehabilitation_charts", {id: this.props.currentChartId}, (result) => {
        this.setState({
        });
      });
  };

  render() {
    return (
      <div>{this.getChart()}</div>
    );
  }
}
