import React, { useEffect } from "react";
import { useState } from "react";
import { GoogleMap, useLoadScript, MarkerF } from "@react-google-maps/api";
import Geocode from "react-geocode";
import Paper from "@mui/material/Paper";
export default function GoogleMaps(props) {
  const { machineChoice, handleDistance } = props;
  const [location, setLocation] = useState({ lat: 3, lng: 3 });
  const [currLocation, setCurrLocation] = useState({ lat: 3, lng: 3 });

  const { isLoaded } = useLoadScript({
    googleMapsApiKey: process.env.REACT_APP_GOOGLE_API,
  });

  useEffect(() => {
    Geocode.setApiKey(process.env.REACT_APP_GOOGLE_API);
    Geocode.setLanguage("he");
    Geocode.setRegion("il");
    Geocode.fromAddress(
      `${machineChoice?.address} , ${machineChoice?.city}`
    ).then(
      (response) => {
        const { lat, lng } = response.results[0].geometry.location;

        setLocation({ lat: lat, lng: lng });
      },
      (error) => {
        console.error(error);
      }
    );

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          };
          setCurrLocation(pos);
        },
        () => {
          console.log("err");
        }
      );
    }
  }, []);

  useEffect(() => {
    function getDistance() {
      if (isLoaded) {
        const google = window.google;
        var service = new google.maps.DistanceMatrixService();
        origin = new google.maps.LatLng(currLocation.lat, currLocation.lng);
        service.getDistanceMatrix(
          {
            origins: [origin],
            destinations: [location],
            travelMode: "DRIVING",
          },
          (response, status) => {
            handleDistance(response.rows[0]?.elements[0]?.distance?.text);
          }
        );
      }
    }
    if (currLocation.lat !== 3 && location.lat !== 3) getDistance();
  }, [currLocation, location]);
  if (!isLoaded) return <div>טוען..</div>;
  return (
    <Paper elevation={12} sx={{ borderRadius: "18px" }}>
      <GoogleMap
        zoom={18}
        center={location}
        mapContainerStyle={{
          height: "300px",
          width: "300px",
          border: "solid",
          borderRadius: "18px",
          borderColor: "#C0C0C0",
        }}
      >
        <MarkerF
          visible={true}
          key={currLocation}
          position={currLocation}
          label="אני"
        />
        <MarkerF
          visible={true}
          key={machineChoice.id}
          position={location}
          label="מכונת PillCenter"
        />
      </GoogleMap>
    </Paper>
  );
}
