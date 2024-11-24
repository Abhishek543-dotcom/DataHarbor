// src/components/TopBar.js
import React from "react";
import { AppBar, Toolbar, Typography, Breadcrumbs, Avatar } from "@mui/material";
import { NavigateNext } from "@mui/icons-material";

const TopBar = () => {
  const breadcrumbs = ["Workspace", "Users", "abhishek16@gmail.com", "SQL"];

  return (
    <AppBar
      position="static"
      sx={{ backgroundColor: "#001F3F", color: "#ffffff", padding: "0 16px" }}
    >
      <Toolbar>
        <Breadcrumbs
          separator={<NavigateNext fontSize="small" style={{ color: "#ffffff" }} />}
          aria-label="breadcrumb"
          sx={{ flexGrow: 1, color: "#ffffff" }}
        >
          {breadcrumbs.map((crumb, index) => (
            <Typography key={index} color="inherit">
              {crumb}
            </Typography>
          ))}
        </Breadcrumbs>
        <Avatar sx={{ backgroundColor: "#FFD700" }}>A</Avatar>
      </Toolbar>
    </AppBar>
  );
};

export default TopBar;
