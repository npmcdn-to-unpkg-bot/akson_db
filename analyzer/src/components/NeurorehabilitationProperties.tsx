import * as React from "react";
// import from "jquery";
import * as $ from "jquery";
import * as bs from "bootstrap-datepicker";

export interface INeurorehabilitationProperties {
  updateCharts: any;
  currentPatientId: number;
  currentChartId?: number;
}

export interface NeurorehabilitationPropertiesState {

}

export default class NeurorehabilitationProperties extends React.Component<INeurorehabilitationProperties, NeurorehabilitationPropertiesState> {
  componentWillMount = () => {
    // $.get("./api/neurorehabilitation_data", {id: this.props.id}, (result) => {
    //   this.props.updateData(result);
    // });
  };

  private exerciseSignatures: Array<any> = [];
  private beginDate: any;
  private endDate: any;

  componentDidMount() {
    console.log($("#start-date"));
    $("#start-date").datepicker();
    console.log($("#start-date"), "end");

  }

  private createDatePicker = () => {
  }

  render() {
    console.log($("#start-date"), "render");
    return (
      <div>
        <p>data poczatkowa<input type="text" id="start-date"/></p>
        {this.createDatePicker()}
      </div>
    );
  }
}
