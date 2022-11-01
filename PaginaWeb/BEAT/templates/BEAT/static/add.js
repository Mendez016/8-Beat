const textAud=document.getElementById('label--audio')
const textImg=document.getElementById('label--imagen')
const inputAud=document.getElementById('audio')
const inputImg=document.getElementById('image')
inputAud.style.opacity=0
inputImg.style.opacity=0
inputAud.onchange=function() {cambio(1)}
inputImg.onchange=function() {cambio(2)}
function cambio(state){
    if(state===1){
        const upFiles=inputAud.files
        if(upFiles.length===0){
            textAud.innerHTML='Audio'
        }else{
            for(const file of upFiles){
                textAud.innerHTML='Nombre archivo: '+file.name
            }
        }
} else if(state===2){
    const upFiles=inputImg.files
    if(upFiles.length===0){
        textImg.innerHTML='Imagen'
    }else{
        for(const file of upFiles){
            textImg.innerHTML='Nombre archivo: '+file.name
        }
    }
}
}