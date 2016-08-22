import * as React from "react";
import * as $ from "jquery"

import PatientCharts from "./PatientCharts"

export interface HelloProps {
  compiler: string;
    framework: string;
}

const enum View {
  MAIN,
  PATIENT,
  CHART
};

export interface PatientsState {
  patients: any[];
  view: View;
  currentPatientId?: number;
}


export class Hello extends React.Component<HelloProps, PatientsState> {
  public state = {
    patients: [{}],
    view: View.MAIN
  };

  componentWillMount = () => {
    $.get("./api/patient", (result) => {
      this.setState({
        patients: result,
        view: View.MAIN
      })
    });
  };

  private onClick = (id: number) => {
    this.setState({
      patients: this.state.patients,
      currentPatientId: id,
      view: View.PATIENT
    });
    console.log("OnClick", id);
  };

  createPatients = () => {
    return this.state && this.state.patients.map((patient: any) => {
      return (
        <div id={patient.id} onClick={this.onClick.bind(this, patient.id)}>
          {patient.id + ". " + patient.first_name + " " + patient.last_name}
        </div>
      )
    });
  };

  private renderChild = () => {
    if(this.state.view === View.MAIN) {
      return (
        <div>
          {this.createPatients()}
        </div>
      );
    } else if (this.state.view === View.PATIENT) {
      return (
        <PatientCharts id={this.state.currentPatientId}/>
      );
    }
    return null;
  };

  render() {

    return (
      <div>
        {this.renderChild()}
      </div>
    );
  }
}
