(function(){
    const btnEliminar=document.querySelectorAll(".btnEliminar");

    btnEliminar.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion=confirm('Seguro quiere eliminar la tarifa?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    })
})();