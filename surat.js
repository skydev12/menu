function gerURL(e){
    const pageURL = window.location.search.substring(1);
    const urlVariable = pageURL.split('&');

    for(let i = 0; i < urlVariable.length; i++){
        const parameterName = urlVariable[i].split('=');
        if(parameterName[0] == e){
            return parameterName[1];
        }
    }
}

const nomorsurat = gerURL('nomorsurat');

function getSurat(){
    fetch(https://equran.id/api/surat/${nomorsurat})
    .then(response => response.json())
    .then(response => {

        // title surat 
        const titleSurat = document.querySelector('#title-surat');
        titleSurat.textContent = 'Surat ${response.nama_latin}'
        // judul surat
        const judulSurat = document.querySelector('.judul-surat');
        const cardJudulSurat = `
        <strong>${response.nama_latin} - ${response.nama}</strong>
        <p>jumlah ayat : ${response.jumlah_ayat} (${response.arti}) </p>
        <button class="btn btn-primary audio-button-play"> 
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-play" viewBox="0 0 16 16">
                <path d="M6 10.117V5.883a.5.5 0 0 1 .757-.429l3.528 2.117a.5.5 0 0 1 0 .858l-3.528 2.117a.5.5 0 0 1-.757-.43z"/>
                <path d="M4 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zm0 1h8a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1"/>
            </svg>
            dengarkan 
        </button>
        <button class="btn btn-danger hidden-button audio-button-pause"> 
           <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-stop-circle" viewBox="0 0 16 16">
  <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
  <path d="M5 6.5A1.5 1.5 0 0 1 6.5 5h3A1.5 1.5 0 0 1 11 6.5v3A1.5 1.5 0 0 1 9.5 11h-3A1.5 1.5 0 0 1 5 9.5z"/>
</svg>
            stop
        </button>
        <audio id="audio-tag" src="${response.audio}"></audio>
        `;
        judulSurat.innerHTML = cardJudulSurat;
        // end judul surat

        // isi surat
        const surat = response.ayat;
        let isiSurat = '';
        surat.forEach( s => {
            isiSurat += `
             <div class="card mb-3">
                    <div class="card-body">
                     <p>${s.nomor}</p>
                     <h3 class="text-end">${s.ar}</h3>
                     <p>${s.tr}</p>
                     <p>${s.idn}</p>
                    </div>
                  </div>
            `;
        });

        const cardIsiSurat = document.querySelector('.card-isi-surat');
        cardIsiSurat.innerHTML = isiSurat;

        //play and pause audio
const buttonPlay = document.querySelector('.audio-button-play');
const buttonPause = document.querySelector('.audio-button-pause');
const audioSurat = document.getElementById('audio-tag');
            
// play
buttonPlay.addEventListener('click', function () {
    buttonPlay.classList.add("hidden-button");
    buttonPause.classList.remove('hidden-button');
    audioSurat.play();
});

// pause
buttonPause.addEventListener('click', function () {
    buttonPlay.classList.remove("hidden-button");
    buttonPause.classList.add('hidden-button');
    audioSurat.pause();
});

 
        console.log(surat);
    });
}
getSurat();
