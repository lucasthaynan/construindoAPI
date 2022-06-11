fetch('https://raw.githubusercontent.com/lucasthaynan/construindoAPI/main/api_teste.json?token=GHSAT0AAAAAABMIDDLESZFNCXGRFFIYFQNMYVFDHIQ')
  .then(response => response.json() )
  .then(data => {
    // console.log(data[0].time)
    // console.log(data[0].posicao)
    // console.log(data[0].pontos)

    console.log(data)

  })