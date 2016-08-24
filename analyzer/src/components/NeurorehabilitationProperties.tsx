import * as React from "react";
import * as $ from "jquery";


export interface INeurorehabilitationProperties {
  updateCharts: any;
  currentPatientId: number;
  currentChartId?: number;
}

export interface NeurorehabilitationPropertiesState {
  signatures: any;
}

export default class NeurorehabilitationProperties extends React.Component<INeurorehabilitationProperties, NeurorehabilitationPropertiesState> {
  public state = {
    signatures: [{}]
  };

  componentWillMount = () => {
    $.get("./api/signature", {}, (result) => {
      this.setState({
        signatures: result
      })
    });
  };

  private exerciseSignatures: Array<any> = [];
  private beginDate: any;
  private endDate: any;

  componentDidMount() {
    $("#start-date").datepicker();
    $(".akson-date").each(function(index, elem) {
      $(elem).datepicker();
    });
  }

  render() {
    return (
      <div>
        <p>data poczatkowa<input type="text" className="akson-date"/></p>
        <p>data koncowa<input type="text" id="start-date" className="akson-date"/></p>
        <p>sygnatury
          <select multiple>
            {this.state.signatures.map((signature: any) => {
              return (
                <option value={signature.name}>{signature.name}</option>
              );
            })}
          </select>
        </p>
      </div>
    );
  }
}
