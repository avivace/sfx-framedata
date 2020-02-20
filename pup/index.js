const puppeteer = require('puppeteer')
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({headless: false})
  const page = await browser.newPage()
  await page.goto('https://steamcommunity.com/openid/login?openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.mode=checkid_setup&openid.return_to=https%3A%2F%2Fgame.capcom.com%2Fcfn%2Fsfv%2Fgate%2Fsteamcallback&openid.realm=https%3A%2F%2Fgame.capcom.com&openid.ns.sreg=http%3A%2F%2Fopenid.net%2Fextensions%2Fsreg%2F1.1&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select')
  await page.type('#steamAccountName', "")
  await page.type('#steamPassword', "")
  await page.click('[id="imageLogin"]')
  await page.waitForNavigation()
  await page.goto('https://game.capcom.com/cfn/sfv/character/juri/frame/table#vt1')
  let bodyHTML = await page.evaluate(() => document.body.innerHTML);
  fs.writeFileSync('test.html', bodyHTML);

  browser.close()
})()
