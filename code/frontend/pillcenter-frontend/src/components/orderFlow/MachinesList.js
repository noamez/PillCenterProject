import { Box } from "@mui/system";
import { Grid } from "@mui/material";
import Item from "../buttons/Item";
import React, { useState, useEffect } from "react";
import axios from "axios";
import { Typography } from "@mui/material";
import LoadingOrder from "../loading/LoadingOrder";

export default function MachinesList(props) {
  const [machines, setMachines] = useState([]);
  const [response, setResponse] = useState(false);
  const { medicineChoice, handleMachineChoose } = props;

  const getMachines = async () => {
    const res = await axios
      .get(`/api/medicineinstock/?q=${medicineChoice}`)
      .then((response) => {
        setMachines(response.data);
        setResponse(true);
      })
      .catch((err) => console.log(err));
  };

  useEffect(() => {
    getMachines();
  }, [medicineChoice]);
  return (
    <center>
      {!response ? (
        <LoadingOrder text="אנא המתן מחפש מכונות באזורך" />
      ) : machines.length > 0 ? (
        <React.Fragment>
          <Typography sx={{ marginTop: 5 }} variant="h5">
            {" "}
            התרופה שבחרת נמצאת במלאי
          </Typography>
          <Typography variant="h5"> מאיפה תרצה לאסוף את התרופה ?</Typography>
          <br></br>
          <Box sx={{ width: "70%" }}>
            <Grid
              container
              rowSpacing={1}
              columnSpacing={{ xs: 1, sm: 1, md: 2 }}
            >
              {machines.map((machine) => {
                return (
                  <Grid item={true} xs={12} key={machine.id}>
                    <Item
                      sx={{
                        border: 1,
                        borderWidth: 3,
                        borderColor: "black",
                        height: 75,
                        lineHeight: "75px",
                      }}
                      onClick={() => handleMachineChoose(machine)}
                    >
                      {machine.address} , {machine.city}
                    </Item>
                  </Grid>
                );
              })}
            </Grid>
          </Box>{" "}
        </React.Fragment>
      ) : (
        <React.Fragment>
          <Typography sx={{ marginTop: 5 }} variant="h5">
            לצערנו התרופה שבחרת אינה נמצאת אצלנו במלאי המכונות
          </Typography>
        </React.Fragment>
      )}{" "}
    </center>
  );
}
