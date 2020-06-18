function f() {
    w = window.innerWidth;
    l = window.innerHeight;
    document.querySelector('header').style.height = String(Math.round(l * 0.0341796875)) + "px";
    document.querySelector('header').querySelector('p').style.fontSize = String(Math.round(w * 0.00902778)) + "px";
    let field = document.querySelector('input');
    field.style.fontSize = String(Math.round(w * 0.0087)) + "px";
    field.style.paddingLeft = String(Math.round(w * 0.01388889)) + "px";
    field.style.width = String(Math.round(w * 0.118056 - w * 0.01388889)) + "px";
    field.style.height = String(Math.round(l * 0.01953125)) + "px";
}

setInterval(f, 1);