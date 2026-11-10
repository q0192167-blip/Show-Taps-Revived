def ed(p,a,b):
    s=open(p).read();assert a in s,p;open(p,'w').write(s.replace(a,b,1))
b='app/src/main/java/'
st=b+'show/taps/settings/StSettings.kt'
s=open(st).read();i=s.rfind('}')
open(st,'w').write(s[:i]+'\n    fun hideTaskCard(c: Context) = prefs(c).getBoolean("hide_task", false)\n    fun setHideTaskCard(c: Context, v: Boolean) { prefs(c).edit().putBoolean("hide_task", v).apply() }\n'+s[i:])
hp=b+'com/rosan/installer/ui/page/miuix/settings/home/MiuixHomePage.kt'
ed(hp,'show.taps.StEngine.startActive(context)','show.taps.StEngine.startActive(context);if(show.taps.settings.StSettings.hideTaskCard(context))(context as? android.app.Activity)?.finishAndRemoveTask()')
pp=b+'com/rosan/installer/ui/page/miuix/settings/preferred/MiuixPreferredPage.kt'
ed(pp,'    var useA11yOverlay by','    var hideCard by remember { mutableStateOf(StSettings.hideTaskCard(context)) }\n    var useA11yOverlay by')
ed(pp,'            item { SmallTitle(stringResource(R.string.backup_settings)) }','            item { Card { MiuixSwitchWidget(title = "\u9690\u85cf\u5361\u7247", checked = hideCard, onCheckedChange = { hideCard = it; StSettings.setHideTaskCard(context, it) }) } }\n            item { SmallTitle(stringResource(R.string.backup_settings)) }')
