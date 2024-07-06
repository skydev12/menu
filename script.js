function getSurat() {
    fetch('https://equran.id/api/surat')
        .then(response => {
            console.log('Status:', response.status);
            console.log('Status Text:', response.statusText);
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.text();  // Menggunakan text() untuk debugging
        })
        .then(text => {
            console.log('Raw response text:', text);
            try {
                const jsonResponse = JSON.parse(text);  // Parsing manual untuk debugging
                console.log('Parsed JSON:', jsonResponse);
                let cardSurat = '';
                jsonResponse.forEach(surat => {
                    cardSurat += `
                    <div class="col-lg-3 col-md-4 col-sm-12">
                        <div class="card mb-3 card-surat">
                            <div class="card-body" onclick="location.href='surat.html?nomorsurat=${surat.nomor}'">
                              <h5 class="card-title">${surat.nomor} ${surat.nama_latin}</h5>
                              <h3 class="card-subtitle mb-2 text-muted text-end">${surat.nama}</h3>
                              <p class="card-text text-end">${surat.arti}</p>
                            </div>
                        </div>
                    </div>
                    `;
                });

                const listSurat = document.querySelector('.row.card-surat');
                listSurat.innerHTML = cardSurat;
            } catch (error) {
                console.error('Error parsing JSON:', error);
            }
        })
        .catch(error => console.error('Error:', error));
}

getSurat();
