
<h2 class="wp-block-heading">前書き</h2>



<p>このリポジトリは、awkコマンドを実行して任意の文字列を空白で分割して表示します</p>



<h2 class="wp-block-heading">インストールする必要のあるコマンド</h2>



<p>特に無し</p>



<h2 class="wp-block-heading">クイックスタート</h2>



<p>awkコマンドを実行して各文字列を出力してみてください</p>



<h3 class="wp-block-heading">ubuntu</h3>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>echo "hello awk command world" | awk '{print $4}'</code></pre>



<h3 class="wp-block-heading">macos</h3>



<p>※MacPortsを使用しています</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>echo "hello awk command world" | awk '{print $4}'</code></pre>



<h3 class="wp-block-heading">windows</h3>



<p>※MSYS2 MINGW64を使用しています</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>echo "hello awk command world" | awk '{print $4}'</code></pre>



<h2 class="wp-block-heading">実行手順</h2>



<h3 class="wp-block-heading">ubuntu</h3>



<details class="wp-block-details"><summary>クリックして詳細を開く</summary>
<h4 class="wp-block-heading">事前確認</h4>



<p>特に無し</p>



<h4 class="wp-block-heading">preinstall</h4>



<p>特に無し</p>



<h4 class="wp-block-heading">コマンド</h4>



<p>以下のコマンドを実行することで詳細の文字列worldが出力されるはずです</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>echo "hello awk command world" | awk '{print $4}'</code></pre>



<details class="wp-block-details"><summary>詳細</summary>
<p class="has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size">world</p>
</details>
</details>



<h3 class="wp-block-heading">macos</h3>



<details class="wp-block-details"><summary>クリックして詳細を開く</summary>
<h4 class="wp-block-heading">事前確認</h4>



<p>特に無し</p>



<p>※macosはMacPortsパッケージマネージャを使用してコマンドを管理します。もしインストールしていない方は以下のリンクからMacPortsのインストール手順をご覧ください</p>



<p>またコマンドに別名を設定して既存の環境と競合しないでコマンドを呼び出せるようにします。</p>



<p>初めてこのブログを利用する方は、以下の2つの記事を参考に環境構築してください</p>



[![MacPortsをインストールするまでの手順](https://ss523971.stars.ne.jp/todo/wp-content/uploads/2025/10/thumbnail_macports_title_1920_1080_2.png,)](https://ss523971.stars.ne.jp/todo/2025/10/02/macports%e3%82%92%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e3%81%99%e3%82%8b%e3%81%be%e3%81%a7%e3%81%ae%e6%89%8b%e9%a0%86/)



[![MacPortsでインストールしたコマンドのエイリアス設定](https://ss523971.stars.ne.jp/todo/wp-content/uploads/2025/10/thumbnail_macports2.png,)](https://ss523971.stars.ne.jp/todo/2025/10/03/macports%e3%81%a7%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e3%81%97%e3%81%9f%e3%82%b3%e3%83%9e%e3%83%b3%e3%83%89%e3%81%ae%e3%82%a8%e3%82%a4%e3%83%aa%e3%82%a2%e3%82%b9%e8%a8%ad%e5%ae%9a/)



<h4 class="wp-block-heading">preinstall</h4>



<p>特に無し</p>



<h4 class="wp-block-heading">コマンド</h4>



<p>以下のコマンドを実行することで詳細の文字列worldが出力されるはずです</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>echo "hello awk command world" | awk '{print $4}'</code></pre>



<details class="wp-block-details"><summary>詳細</summary>
<p class="has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size">world</p>
</details>
</details>



<h3 class="wp-block-heading">windows</h3>



<details class="wp-block-details"><summary>クリックして詳細を開く</summary>
<h4 class="wp-block-heading">事前確認</h4>



<p>特に無し</p>



<p>※windowsはMSYS2 MINGW64で確認しています。もしインストールしていない方は以下のリンクからmsys2のインストール手順をご覧ください</p>



[![[windows] msys2をインストールするまでの手順](https://ss523971.stars.ne.jp/todo/wp-content/uploads/2025/10/msys2_thumbnail_1920_1080.png)](https://ss523971.stars.ne.jp/todo/2025/10/02/windows-msys2%e3%82%92%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e3%81%99%e3%82%8b%e3%81%be%e3%81%a7%e3%81%ae%e6%89%8b%e9%a0%86/)



<h4 class="wp-block-heading"><strong>preinstall</strong></h4>



<p>特に無し</p>



<h4 class="wp-block-heading"><strong>コマンド</strong></h4>



<p>以下のコマンドを実行することで詳細の文字列worldが出力されるはずです</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>echo "hello awk command world" | awk '{print $4}'</code></pre>



<details class="wp-block-details"><summary>詳細</summary>
<p class="has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size">world</p>
</details>
</details>



<h2 class="wp-block-heading">後書き</h2>



<p>$0で分割する前の全体の文字列(hello awk command world)を出力します</p>



<h2 class="wp-block-heading">この記事で使用したコマンドで実行できるお薦め記事</h2>



<h2 class="wp-block-heading">この記事で使用しているキーボード</h2>



<p></p>



<p></p>
