import react from "react";
function Footer()
{
    var currYear  = new Date().getFullYear();
    return(
        
        <footer>

            <p>Copyright &copy;{currYear}</p>
        </footer>
         
        
    );
}
export default Footer;
