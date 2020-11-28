<?php
    $url = block_field('field-url', false); //BlockLabからURLを取得
?>

<div class="blogcard">
    <p>[sitecard url="<?php echo $url; ?>"]</p>
</div>