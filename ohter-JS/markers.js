(function () {
    const { Fragment, createElement } = wp.element;
    const { registerFormatType, toggleFormat } = wp.richText;
    const { RichTextToolbarButton, RichTextShortcut, BlockFormatControls } = wp.editor;
 
    const el = createElement;
 
    const tagTypes = [];
    tagTypes.push({ tag: 'mark', class: 'marker-halfYellow', title: 'mark (アンダーラインマーカー)',icon: 'edit' });
    tagTypes.push({ tag: 'mark', class: 'marker-halfPink', title: 'mark (アンダーラインマーカー)',icon: 'edit' });
    tagTypes.push({ tag: 'mark', class: 'marker-halfBlue', title: 'mark (アンダーラインマーカー)',icon: 'edit' });
 
    tagTypes.map( (idx) => {
        let type = 'celtis/richtext-' + idx.tag;
        if(idx.class !== null){
            type += '-' + idx.class;
        }
        registerFormatType( type, {
            title: idx.title,
            tagName: idx.tag,
            className: idx.class,
 
            edit( { isActive, value, onChange } ) {
                return (
                    el( Fragment,
                        {},
                        el( RichTextToolbarButton,
                            { icon: idx.icon,
                              title: idx.title,
                              isActive: isActive,
                              onClick: () => onChange( toggleFormat(value, { type: type })),
                            }
                        )
                    )
                );
            },
        });
    }) 
});