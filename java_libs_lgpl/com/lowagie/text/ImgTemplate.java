/*
 * $Id: ImgTemplate.java,v 1.20 2002/08/23 08:59:32 blowagie Exp $
 * $Name:  $
 *
 * Copyright 2000, 2001, 2002 by Paulo Soares.
 *
 *
 * The Original Code is 'iText, a free JAVA-PDF library'.
 *
 * The Initial Developer of the Original Code is Bruno Lowagie. Portions created by
 * the Initial Developer are Copyright (C) 1999, 2000, 2001, 2002 by Bruno Lowagie.
 * All Rights Reserved.
 * Co-Developer of the code is Paulo Soares. Portions created by the Co-Developer
 * are Copyright (C) 2000, 2001, 2002 by Paulo Soares. All Rights Reserved.
 *
 * Contributor(s): all the names of the contributors are added in the source code
 * where applicable.
 *
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 * 
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 * 
 * You should have received a copy of the GNU Library General Public
 * License along with this library; if not, write to the
 * Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
 * Boston, MA  02110-1301, USA.
 *
 *
 * If you didn't download this code from the following link, you should check if
 * you aren't using an obsolete version:
 * http://www.lowagie.com/iText/
 */

package com.lowagie.text;

import java.net.URL;
import com.lowagie.text.pdf.PdfTemplate;

/**
 * PdfTemplate that has to be inserted into the document
 *
 * @see		Element
 * @see		Image
 *
 * @author  Paulo Soares
 */

public class ImgTemplate extends Image implements Element {
    
    ImgTemplate(Image image) {
        super(image);
    }
    
    /** Creats an Image from a PdfTemplate.
     *
     * @param template the PdfTemplate
     * @throws BadElementException on error
     */
    public ImgTemplate(PdfTemplate template) throws BadElementException{
        super((URL)null);
        if (template == null)
            throw new BadElementException("The template can not be null.");
        if (template.getType() == PdfTemplate.TYPE_PATTERN)
            throw new BadElementException("A pattern can not be used as a template to create an image.");
        type = IMGTEMPLATE;
        scaledHeight = template.getHeight();
        setTop(scaledHeight);
        scaledWidth = template.getWidth();
        setRight(scaledWidth);
        setTemplateData(template);
        plainWidth = width();
        plainHeight = height();
    }
}