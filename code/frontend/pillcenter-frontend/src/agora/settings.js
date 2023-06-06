import { createClient, createMicrophoneAndCameraTracks } from "agora-rtc-react";
export const appId = process.env.REACT_APP_AGORA_APP_ID;

export const config = { mode: "rtc", codec: "vp8", appId: appId };
export const useClient = createClient(config);
export const useMicrophoneAndCameraTracks = createMicrophoneAndCameraTracks();
export const channelName = "main";
export const CustomerId = "6c7198b759e44cd5bd58ad747299d1a0";
export const secret = "6e8ec06f42a848e39e4d98a7cb683c87";
