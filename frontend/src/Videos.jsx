import React from "react"
import { Avatar, Button, Dialog, DialogActions, DialogTitle, List, ListItem, ListItemAvatar, ListItemText } from "@mui/material"
import OndemandVideoIcon from '@mui/icons-material/OndemandVideo';
import axios from "axios"

export default function Videos({isOpen, setIsOpen, vids = [], query=""}) {

    const [isDialogOpen, setIsDialogOpen] = React.useState(isOpen)
    const [videos, setVideos] = React.useState(vids)

    const handleListItemClick = (videoId) => {
      window.open(
        `http://localhost:8000/videos/${videoId}`, "_blank");
    }

    React.useEffect(() => {
      setIsDialogOpen(isOpen)
    }, [isOpen])

    React.useEffect(() => {
      setVideos(vids)
    }, [vids])

    const handleClose = () => {setIsOpen(false);setIsDialogOpen(false)} 

    return (<Dialog fullWidth onClose={handleClose} open={isDialogOpen}>
        <DialogTitle>Search result for {query}</DialogTitle>
        <List sx={{ pt: 0 }}>
          {
          videos.length <= 0 ? 
          
          (
          
    <ListItem>
          <ListItemText primary="No video found" />
        </ListItem>) : 
          videos.map((video) => (
            <ListItem button onClick={() => handleListItemClick(video.video_uuid)} key={video.video_uuid}>
              <ListItemAvatar>
              <Avatar>
                <OndemandVideoIcon/>
              </Avatar>
            </ListItemAvatar>
              <ListItemText >{`filename : ${video.filename} Score : ${video.score} `}</ListItemText>
            </ListItem>
          ))}
         
        </List>
        <DialogActions>
          <Button onClick={handleClose}>Close</Button>
        </DialogActions>
      </Dialog>)



}