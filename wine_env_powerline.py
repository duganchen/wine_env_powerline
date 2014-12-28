from powerline.theme import requires_segment_info

@requires_segment_info
def bottle(pl, segment_info):
    return segment_info['environ'].get('BOTTLE') or None

