const kirjat = [
    {'nimi': 'Monte Kriston kreivi',
    'kirjailija': 'Alexander Dumas'},
    { 'nimi': 'Sotaromaani',
        'kirjailija': 'Väinö Linna'
    }
];

kirjat.forEach(kirja => {
    let nimi = kirja.nimi;
    let kirjailija = kirja.kirjailija;
    console.log("Kirjan " + nimi + " on kirjoittanut " +
        kirjailija);
})