<?php
    $url = block_field('field-url', false); //BlockLabからURLを取得
    $id = url_to_postid($url);//URLから投稿IDを取得

    $no_image = ''; //指定URLの記事にアイキャッチがない場合、ここで指定した画像を表示する
    if(empty($title)){
        $title = esc_html(get_the_title($id)); //タイトルを取得
    }
    //抜粋文を取得
    if(empty($excerpt)){
        // 記事IDから冒頭文を抜粋
        $post = get_post($id);
        setup_postdata($id);
        $excerpt = get_the_excerpt();
    }

    if(has_post_thumbnail($id)) 
    {
        // アイキャッチがある場合、画像を取得する
        $img = wp_get_attachment_image_src(get_post_thumbnail_id($id), 'full');
        $img_tag = "<img src='" . $img[0] . "' alt='{$title}'/>";
    }
    else
    { 
        // アイキャッチが無い場合、7行目で指定した画像を表示する
        $img_tag ='<img src="'.$no_image.'" alt=""/>';
    }
?>

<div class="cp_card05">
  <?php echo $img_tag; ?>
  <div class="description">
    <div class="content">
      <div class="title"><a href="<?php echo $url; ?>"><?php echo $title ?></a></div>
      <p class="text"><?php echo $excerpt ?></p>
      <a href="<?php echo $url; ?>" class="button">Read more</a>
    </div>
  </div>
</div>