import React, {useState} from 'react'
import "../css/header.css"
import MediaQuery from 'react-responsive';
import Button from '@material-ui/core/Button';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import MenuIcon from '@material-ui/icons/Menu';
import SearchIcon from '@material-ui/icons/Search'
function Header() {

    const [anchorEl, setAnchorEl] = useState(null);

    const handleClick = (event) => {
      setAnchorEl(event.currentTarget);
    };
  
    const handleClose = () => {
      setAnchorEl(null);
    };

    return (
        <div className="header">
            <div className="header__title">
                <span>Store Front</span>
            </div>
            <div className="header__search">
                <SearchIcon className = "header__searchIcon"/>
                <input className="header__searchInput" type="text" label="search"></input>
            </div> 
            <div className="header__options">
                <MediaQuery query="(min-width: 600px)" >
                    <p className="header__option1">Sign In</p>  
                    <p className="header__option2">Cart</p>
                </MediaQuery>
                <MediaQuery query="(max-width: 600px)">
                    <Button className="header__button" aria-controls="simple-menu" aria-haspopup="true" onClick={handleClick}>
                        <MenuIcon className = "header__menuIcon"/>
                    </Button>
                    <Menu
                        id="simple-menu"
                        anchorEl={anchorEl}
                        keepMounted
                        open={Boolean(anchorEl)}
                        onClose={handleClose}
                    >
                        <MenuItem onClick={handleClose}>Sign In</MenuItem>
                        <MenuItem onClick={handleClose}>Cart</MenuItem>
                    </Menu>
                </MediaQuery>
            </div>
                
        </div>
    )
}

export default Header
