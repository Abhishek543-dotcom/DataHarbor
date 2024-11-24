// src/components/Sidebar.js
import React from "react";
import { Drawer, List, ListItem, ListItemIcon, ListItemText } from "@mui/material";
import { Home, Search, Storage, Settings } from "@mui/icons-material";

const Sidebar = () => {
  const menuItems = [
    { text: "Workspace", icon: <Home /> },
    { text: "Recents", icon: <Search /> },
    { text: "Catalog", icon: <Storage /> },
    { text: "Settings", icon: <Settings /> },
  ];

  return (
    <Drawer
      variant="permanent"
      sx={{
        width: 240,
        flexShrink: 0,
        "& .MuiDrawer-paper": {
          width: 240,
          backgroundColor: "#002B4F",
          color: "#ffffff",
        },
      }}
    >
      <List>
        {menuItems.map((item, index) => (
          <ListItem button key={index}>
            <ListItemIcon sx={{ color: "#ffffff" }}>{item.icon}</ListItemIcon>
            <ListItemText primary={item.text} />
          </ListItem>
        ))}
      </List>
    </Drawer>
  );
};

export default Sidebar;
