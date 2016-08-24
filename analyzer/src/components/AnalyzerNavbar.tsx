import * as React from "react";
import * as $ from "jquery";


export interface AnalyzerNavbarState {
  id?: number;
  patients: any;
}

export interface AnalyzerNavbarProps {
  newChart: any; // TODO React.PropTypes.func;
  selectChart: any; // TODO React.PropTypes.func;
};

export default class AnalyzerNavbar extends React.Component<AnalyzerNavbarProps, AnalyzerNavbarState> {
  public state = {
    patients: [{}]
  };

  componentWillMount = () => {
    $.get("./api/patient", (result) => {
      this.setState({
        id: null,
        patients: result
      })
    });
  };

  newChartForPatient = (patientId: number) => {
    this.props.newChart(patientId);
  };

  renderPatients = () => {
    return (
      <div id="navbar">
        {this.state.patients.map((patient: any) => {
          return (
            <div>
              <div onClick={this.props.selectChart}>
                {patient.last_name + " " + patient.first_name}
              </div>
              <button onClick={this.newChartForPatient.bind(this, patient.id)}>+</button>
            </div>
          );
        })}
      </div>
    );
  }


  render() {
    return (
      <div>{this.renderPatients()}</div>
    );
  }
}
