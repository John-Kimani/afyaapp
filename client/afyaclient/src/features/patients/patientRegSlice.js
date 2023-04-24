import { createSlice } from "@reduxjs/toolkit";

const patientSlice = createSlice({
    name: 'patientRegistration',
    initialState: {
        patientInformation: null
    },
    reducers: {
        registerNewPatient: (state, action) => {
            state.patientInformation = action.payload
        }
    }
});

export const { registerNewPatient } = patientSlice.actions;
export default patientSlice.reducer;