# Basic Info

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic WakaTime Badge</title>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>

<script>
    async function refreshWakaTimeBadge() {
        const username = 'matixandr09'; // Replace with your GitHub username
        const period = 'month'; // Specify the time period for stats (optional)

        const response = await axios.get(`https://github-readme-stats.vercel.app/api/wakatime?username=${username}${period ? `&period=${period}` : ''}`);
        const badgeUrl = response.data.badgeUrl;

        const badgeImage = document.getElementById('wakatime-badge');
        badgeImage.src = badgeUrl;
    }

    // Refresh the badge on page load
    refreshWakaTimeBadge();

    // Refresh the badge every 5 minutes (optional)
    setInterval(() => {
        refreshWakaTimeBadge();
    }, 300000); // 5 minutes in milliseconds
</script>

<img id="wakatime-badge" src="" alt="WakaTime stats badge">

</body>
</html>

Hello everyone here you can find for free my scripts that i made in python and more! Feel free to give sugesstions

[![MatixAndr09's WakaTime stats](https://github-readme-stats.vercel.app/api/wakatime?username=matixandr09)](https://github.com/anuraghazra/github-readme-stats)![MatixAndr's github stats](https://github-readme-stats.vercel.app/api?username=matixandr09&show_icons=true&theme=radical)

# Current Available Scripts

<img src="https://cdn.discordapp.com/attachments/1174656852596903976/1174656875153866762/Bez_nazwy-1.png?ex=65686377&is=6555ee77&hm=fb9c06a56d067121eec3ba767c715cd1f13bb0b1167df48b6974caa08b3eef5a" width="16" height="16" alt="tcp"> **Python Scripts**
  - 📰 *File Logger*
  - 🌐 *Webpage Info*
  - ⌨️ *Combinations Writer*
