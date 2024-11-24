// src/App.js
import React from "react";
import Sidebar from "./components/Sidebar";
import TopBar from "./components/TopBar";
import WorkspaceTable from "./components/WorkspaceTable";
import { CssBaseline } from "@mui/material";

const App = () => {
  return (
    <>
      {/* Add global styling reset */}
      <CssBaseline />

      <div style={{ display: "flex", height: "100vh" }}>
        {/* Sidebar component */}
        <Sidebar />

        {/* Main content */}
        <div style={{ flex: 1, display: "flex", flexDirection: "column", backgroundColor: "#F5F5F5" }}>
          {/* Top navigation bar */}
          <TopBar />

          {/* Workspace content */}
          <div style={{ padding: "16px", flex: 1 }}>
            <WorkspaceTable />
          </div>
        </div>
      </div>
    </>
  );
};

export default App;
