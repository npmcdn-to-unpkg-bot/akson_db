import * as React from "react";
import * as $ from "jquery"

export interface HelloProps {
  compiler: string;
    framework: string; }


export class Hello extends React.Component<HelloProps, {}> {

    componentWillMount = () => {
      $.get("./analyzer/api/patients", (result) => {
          console.log(result);
      })
    };

    render() {
        return (
          <select>
              <option value="volvo">Volvo</option>
              <option value="saab">Saab</option>
              <option value="vw">VW</option>
              <option value="audi" selected>Audi</option>
          </select>
        );
    }
}
