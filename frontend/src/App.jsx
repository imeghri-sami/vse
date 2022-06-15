import React from "react"
import Logo from "./Logo";
import { Box, Button, Input } from "@mui/material";
import Videos from "./Videos";
import TextField from "@mui/material/TextField";
import axios from "axios";

export default function App() {

    const [isDisabled, setIsDisabled] = React.useState(false)
    const input = React.useRef(null)
    
    const [videos, setVideos] = React.useState([])
    const [value, setValue] = React.useState("")
    const [open, setOpen] = React.useState(false)
    const [selected, setSelected] = React.useState(null) 
    const search = () => {

      if(value){
        axios.
        get(`/search?query=${value}`)
        .then(res => {setVideos(res.data);setOpen(true) })
        .catch(err => alert("ERROR : fetching videos"))
      }
          
    } 

    const upload = (e) => {
      if(!selected) return;

      setIsDisabled(true)
      const formData = new FormData();
      formData.append("file", selected);

      axios({
        method: "post",
        url: "/upload-video",
        data: formData,
        headers: {
          "Content-Type": "multipart/form-data"
        }
      }).then(res => {setIsDisabled(false);setSelected(null); console.log(res.data)})
      .catch(err => {setIsDisabled(false);setSelected(null);alert("ERROR : Uploading file")})

    }
    const handleFileChange = (e) => {
      setSelected(e.target.files[0])
    }

    return (<Box
    sx={{
      width: "100vw",
      height: "100vh",
      display: "flex",

      justContent: "center",
      alignItems: "center",
    }}
  >
    <Box
      px={16}
      sx={{
        width: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <Logo />
      <TextField error={true} value={value} onChange={(e) => setValue(e.target.value)} fullWidth id="search-bar" />
      <div style={{marginTop: "8px"}}>
        <Button
          sx={{ marginRight: "8px" }}
          label="test"
          variant="contained"
          onClick={search}
        >
          Search
        </Button>
        <label htmlFor="contained-button-file">
          <Input
            ref={input}
            disabled={isDisabled}
            sx={{ display: "none" }}
            accept="video/*"
            id="contained-button-file"
            type="file"
            onChange={handleFileChange}
          />
          <Button onClick={upload} disabled={isDisabled} variant="outlined" component="span">
            {isDisabled ? "Processing ..." : "upload a video    "}
          </Button>
        </label>
        <Videos isOpen={open} setIsOpen={setOpen} vids={videos} query={value}/>
      </div>
    </Box>
  </Box>)
}