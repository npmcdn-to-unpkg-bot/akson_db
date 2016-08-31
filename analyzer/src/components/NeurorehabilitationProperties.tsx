import * as React from "react";
import * as $ from "jquery";


export interface INeurorehabilitationProperties {
  updateCharts: any;
  currentPatientId: number;
  currentChartId?: number;
}

export interface NeurorehabilitationPropertiesState {
  exerciseSignatures: any;
  valueTypes: any;
}

export default class NeurorehabilitationProperties extends React.Component<INeurorehabilitationProperties, NeurorehabilitationPropertiesState> {
  public state = {
    exerciseSignatures: [{}],
    valueTypes: [{}]
  };

  componentWillMount = () => {
    $.get("./api/excercise_signature", {}, (result) => {
      var signatures = result;
      // TODO promise or something?
      $.get("./api/neurorehabilitation_data/fields", {}, (result) => {
        this.setState({
          exerciseSignatures: signatures,
          valueTypes: result
        });
      });
    });
  };

  componentDidMount() {
    $("#begin-date").datepicker({
      onSelect: this.changeBeginDate.bind(this),
      dateFormat: 'yy-mm-dd'
     });
    $("#end-date").datepicker({
      onSelect: this.changeEndDate.bind(this),
      dateFormat: 'yy-mm-dd'
     });
  }

  private beginDate: any;
  private endDate: any;
  private exerciseSignatures: Array<any> = [];
  private valueTypes: Array<any> = [];

  changeValueTypes(event: any) {
    this.valueTypes = [].filter.call(event.target.options, function (o: any) {
      return o.selected;
    }).map(function (o: any) {
      return o.value;
    }).reduce(function (res: any, el: any) {
      return res + " " + el;
    });
    console.log(this.valueTypes);
    this.loadData();
  }

  changeBeginDate(newDate: any) {
    this.beginDate = newDate;
    console.log(this.beginDate);
    this.loadData();
  }

  changeEndDate(newDate: any) {
    this.endDate = newDate;
    console.log(this.endDate);
    this.loadData();
  }

  changeExcerciseSignatures(event: any) {
    this.exerciseSignatures = [].filter.call(event.target.options, function (o: any) {
      return o.selected;
    }).map(function (o: any) {
      return o.value;
    }).reduce(function (res: any, el: any) {
      return res + " " + el;
    });
    console.log(this.exerciseSignatures);
    this.loadData();
  }

  loadData() {
    var request = {
      patient_id: this.props.currentPatientId,
      begin_date: this.beginDate,
      end_date: this.endDate,
      excercise_signatures: this.exerciseSignatures,
      fields: this.valueTypes
    };

    console.log("loading neurorehabilitation_data with request: " + request);
    $.get("./api/neurorehabilitation_data/", request, (result) => {
      console.log("loaded neurorehabilitation_data");
      console.log(result);
      this.props.updateCharts(result);
    });
  }

  render() {
    return (
      <div>
        <p>data poczatkowa<input type="text" id="begin-date"/></p>
        <p>data koncowa<input type="text" id="end-date"/></p>
        <p>sygnatury
          <select multiple onChange={this.changeExcerciseSignatures.bind(this)}>
            {this.state.exerciseSignatures.map((signature: any) => {
              return (
                <option value={signature.id}>{signature.name}</option>
              );
            })}
          </select>
        </p>
        <p>typ wartosci
          <select multiple onChange={this.changeValueTypes.bind(this)}>
            {this.state.valueTypes.map((valueType: any) => {
              return (
                <option value={valueType.id}>{valueType.name}</option>
              );
            })}
          </select>
        </p>
      </div>
    );
  }
}
