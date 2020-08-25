import React from 'react'
import "../css/Product.css"
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import AddIcon from '@material-ui/icons/Add';
import EditIcon from '@material-ui/icons/Edit';
import DeleteIcon from '@material-ui/icons/Delete';



function Product({ name, price, image}) {
    return (
        <div className="product">
            <Card className="product__card">
                <CardActionArea>
                    <CardContent className = "product__info">
                        <p className="product__name">{name}</p>
                        <p className="product__price">
                            <strong>
                                $
                            </strong>
                            {price}
                        </p>
                        <img className ="product__image" src={image} />
                    </CardContent>
                </CardActionArea>
                <CardActions className = "product__actions">
                    <Button onClick=''> <AddIcon className="product__buttonAdd"/> </Button>
                    <Button onClick=''> <EditIcon className="product__buttonEdit"/> </Button>
                    <Button onClick=''> <DeleteIcon className="product__buttonDel"/> </Button>
                </CardActions>
            </Card>
        </div>
    )
}

export default Product
