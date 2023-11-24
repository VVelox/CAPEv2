domain_passlist_re = [
    # Certificate Trust Update domains
    r"^ocsp\.usertrust\.com$",
    r"\.windows\.com$",
    r"\.windowsupdate\.com$",
    r"^ocsp\.comodoca\.com$",
    r"^crl\.microsoft\.com$",
    r"^urs\.microsoft\.com$",
    r"\.microsoft\.com$",
    r"\.skype\.com$",
    r"\.live\.com$",
    r"clients[0-9]+\.google\.com$",
    r"\.googleapis\.com$",
    r"\.gvt1\.com$",
    r"\.msftncsi\.com$",
    r"^apps\.identrust\.com$",
    r"^isrg\.trustid\.ocsp\.identrust\.com$",
    r"^urs\.microsoft\.com$",
    r"^config\.edge\.skype\.com$",
    r"^client-office365-tas\.msedge\.net$",
    r"ecs\.office\.com$",
    r"^files\.acrobat\.com$",
    r"^acroipm2\.adobe\.com$",
    r"^acroipm\.adobe\.com$",
    r"^ocsp\.trust-provider\.com$",
    r"^ocsp\.comodoca4\.com$",
    r"^ocsp\.pki\.goog$",
    r"^oneclient.sfx.ms$",
    r"^ocsp\.verisign\.com$",
    r"^s2\.symcb\.com$",
    r"^sv\.symcd\.com$",
    r"^s\.symcd\.com$",
    r"^ts-ocsp\.ws\.symantec\.com$",
    r"^ocsp\.thawte\.com$",
    r"^crl\.thawte\.com$",
    r"^crt\.comodoca\.com$",
    r"^crt\.usertrust\.com$",
    r"^ocsp\.sectigo\.com$",
    r"^crl\.globalsign\.net$",
    r"^cacerts\.digicert\.com$",
    r"^ocsp\.digicert\.com$",
    r"^crl3\.digicert\.com$",
    r"^crl4\.digicert\.com$",
    r"\.amazontrust\.com$",
    r"\.opera\.com",
    r"\.ss2\.us$",
    r"\.google-analytics\.com$",
    r"\.googletagmanager\.com$",
    r"^stats\.g\.doubleclick\.net$",
    r"^www\.google\.com$",
    r"^cdn\.amplitude\.com$",
    r"\.msn\.com",
    r"\.operacdn\.com$",
    r"^cdn\.jsdelivr\.net",
    r"^fonts\.gstatic\.com$",
    r"\.edgesuite\.net$",
    r"^www\.bing\.com$",
    r"^api\.bing\.com$",
    r"^crl\.pki\.goog$",
    r"^crl\.identrust\.com$",
    r"^r3\.o\.lencr\.org$",
    r"^x1\.c\.lencr\.org$",
    r"^pki\.goog$",
    r"^trustocean\.crt\.sectigo\.com$",
    r"^statuse\.digitalcertvalidation\.com$",
    r"certificates\.intel\.com",
    r"nsatc\.net",
    r"akamaiedge\.net",
    r"edgekey\.net",
    r"trafficmanager\.net",
    r"hwcdn\.net",
    r"akamai\.net",
    r"akadns\.net",
    r"v0cdn\.net",
    r"msecnd\.net",
    r"crl\.verisign\.com",
    r"e-msedge\.net",
    r"edgecastdns\.net",
    r"swupmf\.adobe\.com",
    r"officeapps\.live\.com",
    r"ocsp\.godaddy\.com",
    r"digicert\.com",
    r"identrust\.com",
    r"dns\.msftncsi\.com",
    r"wpad",
    r"teredo\.ipv6\.microsoft\.com",
    r"rt\.microsoft\.com",
    r"isatap",
    r"ipv6.msftncsi\.com",
    r"mozilla\.org",
    r"mozilla\.com",
    r"office\.net",
]


domain_passlist = [
    # Certificate Trust Update domains
    "ocsp.usertrust.com",
    "windows.com",
    "time.windows.com",
    "ocsp.comodoca.com",
    "ctldl.windowsupdate.com",
    "www.download.windowsupdate.com",
    "crl.microsoft.com",
    "urs.microsoft.com",
    "microsoft.com",
    "skype.com",
    "live.com",
    "nsatc.net",
    "akamaiedge.net",
    "edgekey.net",
    "trafficmanager.net",
    "hwcdn.net",
    "akamai.net",
    "akadns.net",
    "v0cdn.net",
    "msecnd.net",
    "crl.verisign.com",
    "e-msedge.net",
    "edgecastdns.net",
    "swupmf.adobe.com",
    "officeapps.live.com",
    "ocsp.godaddy.com",
    "digicert.com",
    "identrust.com",
    "dns.msftncsi.com",
    "wpad",
    "teredo.ipv6.microsoft.com",
    "rt.microsoft.com",
    "isatap",
    "ipv6.msftncsi.com",
    "clients0.google.com",
    "clients1.google.com",
    "clients2.google.com",
    "clients3.google.com",
    "clients4.google.com",
    "clients5.google.com",
    "clients6.google.com",
    "clients7.google.com",
    "clients8.google.com",
    "clients9.google.com",
    "googleapis.com",
    "gvt1.com",
    "msftncsi.com",
    "apps.identrust.com",
    "isrg.trustid.ocsp.identrust.com",
    "urs.microsoft.com",
    "config.edge.skype.com",
    "client-office365-tas.msedge.net",
    "ecs.office.com",
    "files.acrobat.com",
    "acroipm2.adobe.com",
    "acroipm.adobe.com",
    "ocsp.trust-provider.com",
    "ocsp.comodoca4.com",
    "ocsp.pki.goog",
    "oneclient.sfx.ms",
    "ocsp.verisign.com",
    "s2.symcb.com",
    "sv.symcd.com",
    "s.symcd.com",
    "ts-ocsp.ws.symantec.com",
    "ocsp.thawte.com",
    "crl.thawte.com",
    "crt.comodoca.com",
    "crt.usertrust.com",
    "ocsp.sectigo.com",
    "crl.globalsign.net",
    "cacerts.digicert.com",
    "ocsp.digicert.com",
    "crl3.digicert.com",
    "crl4.digicert.com",
    "amazontrust.com",
    "opera.com",
    "ss2.us",
    "google-analytics.com",
    "googletagmanager.com",
    "stats.g.doubleclick.net",
    "www.google.com",
    "cdn.amplitude.com",
    "msn.com",
    "operacdn.com",
    "cdn.jsdelivr.net",
    "fonts.gstatic.com",
    "edgesuite.net",
    "www.bing.com",
    "api.bing.com",
    "crl.pki.goog",
    "crl.identrust.com",
    "r3.o.lencr.org",
    "x1.c.lencr.org",
    "pki.goog",
    "trustocean.crt.sectigo.com",
    "statuse.digitalcertvalidation.com",
    "certificates.intel.com",
    "hostonly.hostonly",
]
